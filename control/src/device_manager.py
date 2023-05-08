
import time
import logging
from enum import Enum
import threading
from .driver.bsp_underwater_acoustic_comm import mUnderwaterAscousticCommDevice

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
        self.device_property    = device_property
        self.device_description = device_description
        
        # 解析device_property属性字段

        self.storage_filepath   = storage_filepath


        # init device obj according to identify
        self.device_obj        = None
        self.is_Open           = False
        if self.identify    == "satellite":
            self.device_obj = mSatelliteDevice(self.device)
        elif self.identify  == "underwateracoustic":
            self.device_obj = mUnderwaterAscousticCommDevice(self.device)
        else:
            # TODO 添加设备
            pass

        # create device write lock
        self._wlock        = threading.Lock()
        
    def __repr__(self):
        return '设备(%r)' % (self.description)
    
    """ 打开设备            """
    def open(self):
        try:
            self.device_obj.open()
            if not self.device_obj.isOpen():
                raise
            self.is_Open       = True
            logging.info(f"SUCCESS : open device{self}")
        except Exception as e:
            logging.error(f"ERROR   : {self} try to open device")
            self.device_obj = None

    """ 关闭设备            """
    def close(self):
        try:
            if self.device_obj:
                self.device_obj.close()
        except Exception as e:
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
            print(f"ERROR   : {self} try to write data")
            return -1

    """ 检测设备是否可读     """
    def isReadable(self):
        try: 
            if self.is_Open and self.device_obj.isOpen():
                return self.device_obj.isReadable()
        except Exception as e:
            print(f"ERROR   : {self} try to detect device is readable")

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

    """ 添加设备                    """
    def add(self, dev: mDevice):
        self.dev_list.append(dev)

    """ TODO 查询指定设备           """
    def query(self, dev: mDevice):
        pass

    """ TODO 删除指定设备           """
    def delete(self, ddev: mDevice):
        pass

    """ TODO 更新所有设备的HELLO    """
    def update(self):
        pass

    """ 关闭所有设备                """
    def close(self):
        try:
            for dev in self.dev_list:
                dev.close()
        except Exception as e:
            logging.error("ERROR   : Close Device List ", e)
        finally:
            del self.dev_list


""" 从配置文件中加载设备信息    """
def load_device_from_config_file(file_name):
    dev_list = []
    with open(file_name, "r", encoding="utf-8") as f:
        while True:
            rdata = f.readline().replace("\n","")
            if rdata:
                if not "#" in rdata:
                    param1, param2, param3, param4, param5, param6 = rdata.replace(" ","").split(",")
                    dev_list.append(mDevice(device_id=param1, device=param2, identify=param3, type=conv_from_str_to_enum(mDevcieTypeEnum, param4), storage_filepath=param5, description=param6))
            else:
                break
    return dev_list

def load_device_from_db():
    dev_list = []
    
    # 查询数据库
    devices_db = session.query(Device_Model).all()
    for dev in devices_db:
        dev_list.append(mDevice(dev.device_id, dev.device_name, dev.device_type, dev.device_status, dev.device_property, dev.device_description))

    return dev_list