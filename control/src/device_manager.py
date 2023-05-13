
import time
import logging
from enum import Enum
import threading
from .driver.bsp_underwater_acoustic_comm   import mUnderwaterAscousticCommDevice
from .driver.bsp_satellite_comm             import mSatelliteCommDevice

# from driver.msatellite import *
from .tool.mlocaltime   import *
from .tool.mformatconv  import *
from .models.model      import *

""" devcie type enum    """
class mDevcieTypeEnum(Enum):
    TYPE_ELSE     = "else"
    TYPE_SERIAL   = "serial"
    TYPE_ETHERNET = "ethernet"

"""_summary_
achieve device class
Args:
    device              : device
    identify            : the indentify of device
    type                : devcie type, serial, ethernet, file
    storage_filepath    : save device read data
    description         : device descirption
"""
class mDevice(object):
    """ init param and create device object  """
    def __init__(self, device_id: int, device_name: str, device_type: str, device_status: int, device_property: str, device_description: str):
        self.device_id          = device_id
        self.device_name        = device_name
        self.device_type        = device_type
        self.device_status      = device_status
        self.device_property    = eval(device_property)
        self.device_description = device_description

        # 解析device_property属性字段
        self.device_interface   = self.device_property.get("interface")
        self.storage_filepath   = self.device_property.get("storage_filepath")

        # init device obj according to identify
        self.device_obj        = None
        self.is_Open           = False
        self._wlock            = threading.Lock()               # device write lock
        if self.device_name    == "satellite comm module":
            self.device_obj = mSatelliteCommDevice(self.device_interface)
        elif self.device_name  == "underwater acoustic comm module":
            self.device_obj = mUnderwaterAscousticCommDevice(self.device_interface)
        else:
            # TODO 添加设备
            pass

    def __repr__(self):
        return '设备(%r)' % (self.device_description)

    """ 打开设备            """
    def open(self):
        try:
            self.device_obj.open()
            if not self.device_obj.isOpen():
                raise
            self.is_Open       = True
            logging.critical(f"SUCCESS : open device {self}")
        except Exception as e:
            logging.error(f"ERROR   : {self} try to open device")
            self.device_obj = None

    """ 关闭设备            """
    def close(self):
        try:
            if not self.device_obj:
                raise
    
            self.device_obj.close()
            self.device_obj = None
            self.is_Open    = False
            logging.critical(f"SUCCESS : close device {self}")
        except Exception as e:
            self.is_Open        = False
            logging.error(f"ERROR   : {self} try to close device")

    """ 向设备写入数据      """
    def write(self, file_path, file_name):
        try:
            if self.is_Open and self.device_obj.isOpen():
                self._wlock.acquire()                                       # acquire write lock
                file_size = self.device_obj.write(file_path, file_name)     # write file to device
                self._wlock.release()                                       # release write lock
                return file_size
            else:
                raise
        except Exception as e:
            logging.error(f"ERROR   : {self} try to write data")
            return -1

    """ 检测设备是否可读     """
    def isReadable(self):
        try: 
            if self.is_Open and self.device_obj.isOpen():
                return self.device_obj.isReadable()
        except Exception as e:
            logging.error(f"ERROR   : {self} try to detect device is readable")

    """ 从设备读取数据       """
    def read(self, file_path):
        try:
            if self.is_Open and self.device_obj.isOpen():
                if self.device_obj.isReadable():
                    file_name = self.device_obj.read(file_path)
                    if file_name:
                        return file_name
                    else:
                        return None
                else:
                    logging.info(f"{self}没有数据可读")
            else:
                raise
        except Exception as e:
            print(f"ERROR   : {self} read data")

"""_summary_
achieve device list
"""
class mDeviceList(object):
    def __init__(self):
        # create device list
        self.dev_list = []
    
    def __repr__(self):
        return f"设备列表{self.size()}"

    """ 检测设备列表中设备个数      """
    def size(self):
        return len(self.dev_list)

    """ 添加设备                   """
    def add(self, dev: mDevice):
        self.dev_list.append(dev)

    """ 查询指定设备                """
    def query(self, dev_id: int):
        for dev in self.dev_list:
            if dev.device_id == dev_id:
                return dev
        return None

    """ TODO 删除指定设备           """
    def delete(self, dev: mDevice):
        pass

    """ 关闭所有设备                """
    def close(self):
        try:
            for dev in self.dev_list:
                dev.close()
        except Exception as e:
            logging.error(f"ERROR   : Close Device List {e}")
        finally:
            del self.dev_list


""" 从数据库中加载设备信息    """
def load_device_from_db():
    dev_list = []
    
    # 查询数据库
    devices_db = session.query(Device_Model).all()
    for dev in devices_db:
        dev_list.append(mDevice(dev.device_id, dev.device_name, dev.device_type, dev.device_status, dev.device_property, dev.device_description))

    return dev_list