
import os
import math
import logging
from enum import Enum
from ..utils.get_time import get_current_time_apply_to_filename
from .mserial    import *

class mCommCmd(Enum):
    CMD_FILEINFO    = b'\x01'
    CMD_FILEDATA    = b'\x03'
    CMD_ACK         = b'\x04'
    UNKNOWN         = b'\x05'

class mCommAckType(Enum):
    FILEINFO_RECEIVED = b'fileinfo_received'

'''
description:    实现了水声通信设备的驱动，其通信接口为串口设备，
                每次固定发送54个字节，以0x55 0x3F为数据头，接收端以0x56为标识。
'''
class mUnderwaterAscousticCommDevice(object):
    """ init device   """
    def __init__(self, serial_port, serial_baudrate=115200, serial_timeout=5):
        # set parameters
        self.serial_port        = serial_port
        self.serial_baudrate    = serial_baudrate
        self.serial_timeout     = serial_timeout

        # defconfig
        self.PACKET_LEN         = 57                                # 数据帧长度57 = 起始位3 + 命令位1 + 数据位51 + 结束位2
        self.PACKET_CMD_LEN     = 1
        self.PACKET_DATA_LEN    = 51
        self.PACKET_HEADER      = b'\x55\xAA\x36'                   # 起始位
        self.PACKET_HEADER_LEN  = len(self.PACKET_HEADER)
        self.PACKET_END         = b'\x0D\x0A'                       # 结束位
        self.PACKET_ACK         = b'\x66\xBB'                       # ACK
        self.PACKET_ACK_END     = b'\xBB'

        # init defconfig
        self.serial_obj         = None
        self.is_open            = False

    def __repr__(self):
        return '水声通信设备(端口%r 状态%r)' % (self.serial_port, self.is_open)

    """ 检测设备是否在线  """
    def isOpen(self):
        return self.is_open and self.serial_obj.is_open

    """ 检测设备是否可读  """
    def isReadable(self):
        return self.isOpen() and self.serial_obj.inWaiting() != 0

    """ 打开设备         """
    def open(self):
        try:
            if not detectPortIsExisted(self.serial_port):
                raise

            self.serial_obj = serial.Serial(port=self.serial_port, baudrate=self.serial_baudrate, timeout=self.serial_timeout)
            self.is_open    = True
        except Exception as e:
            logging.error(f"ERROR   : {self} try to open failed")

    """ 关闭设备             """
    def close(self):
        try:
            if not self.isOpen():
                raise

            self.serial_obj.close()
            self.is_open    = False
        except Exception as e:
            logging.error(f"ERROR   : {self} try to close device")


    """ 写入文件             """
    def write(self, file_path, file_name):
        log_err = ""
        try:
            # TODO 传输文件信息，不能超过57比特
            file_size = str(os.path.getsize(file_path+file_name))
            self._write_bytes(cmd=mCommCmd.CMD_FILEINFO.value, data=bytes(file_name+"-"+file_size, 'utf-8'))
            # TODO 等待ACK文件大小
            ack_type, ack_data = self._read_bytes()
            if ack_type != mCommCmd.CMD_ACK and mCommAckType.FILEINFO_RECEIVED.value not in ack_data:
                log_err += "未接收到正确的ACK FILEINFO_RECEIVED"
                raise TimeoutError

            # TODO 传输文件数据
            with open(file_path+file_name, 'rb') as file_obj:
                data = file_obj.read()
                self._write_bytes(cmd=mCommCmd.CMD_FILEDATA.value, data=data)

            return file_size
        except Exception as e:
            logging.error(f"{self}传输文件时发生错误, 错误原因：{e} {log_err}")
            return -1

    """ 读取文件             """
    def read(self, file_path):
        # TODO 接收到缓存处理
        log_err = ""
        try:
            if not self.isReadable():
                raise

            try:
                # TODO 接收文件信息
                ack_type, ack_data = self._read_bytes()
                if ack_type != mCommCmd.CMD_FILEINFO:
                    log_err += "未接收到正确的CMD_FILEINFO"
                    raise TimeoutError
                # 解析文件名
                file_info = ack_data.replace(b'\x00',b'').decode("utf-8").split("-")
                if len(file_info) == 2:
                    file_name = file_info[0]
                    file_size = int(file_info[1])
                    # TODO 发送ACK文件信息
                    self._write_bytes(cmd=mCommCmd.CMD_ACK.value, data=mCommAckType.FILEINFO_RECEIVED.value)
                else:
                    log_err += "未解析出正确的文件名和文件大小信息"
                    raise

                # TODO 接收文件数据
                rec_times = math.ceil(file_size / self.PACKET_DATA_LEN)
                rec_data  = b''
                for _ in range(rec_times):
                    idx_type, idx_data = self._read_bytes()
                    if idx_type != mCommCmd.CMD_FILEDATA:
                        log_err += "未接收到正确的CMD_FILEDATA"
                        raise ValueError
                    rec_data += idx_data
                # 写入文件
                rece_file_name = f'REC_{file_name}_{get_current_time_apply_to_filename()}'
                with open(file_path+rece_file_name, 'ab') as file_obj:
                    file_obj.write(rec_data)
                return rece_file_name
            except Exception as e:
                logging.error(f"{self}读取文件发生错误, 错误原因：{e} {log_err}")
                return None
        except Exception as e:
            logging.warning(f"{self}没有数据可读, 警告原因：{e} {log_err}")
            return None

    """ 向设备写入字节数据    """
    def _write_bytes(self, cmd, data):
        try:
            if not self.isOpen():
                raise

            """ 处理bytes数据流，分割成固定长度54个字节，每个帧头为0x55 0xAA 0x36，发送成功接收0x66 0x6B """
            remainder = len(data) % self.PACKET_DATA_LEN
            if(remainder != 0):
                data += b'\x00'*(self.PACKET_DATA_LEN-remainder)

            for idx in range(int(len(data)/self.PACKET_DATA_LEN)):
                # 获取数据帧
                sep = data[idx*self.PACKET_DATA_LEN:(idx+1)*self.PACKET_DATA_LEN]

                # 添加帧头和帧尾
                sep = self.PACKET_HEADER + cmd + sep
                sep = sep + self.PACKET_END
                self.serial_obj.write(sep)
                logging.critical(f"{self}传输一帧数据{sep}")

                # 等待串口回馈确认消息
                ret = self.serial_obj.read_until(expected=self.PACKET_ACK_END)
                if ret and len(ret) == 2 and ret == self.PACKET_ACK:
                    logging.warning(f"{self} 发送数据时接收到0X66 0XBB确认回馈")
                else:
                    # TODO 没有接收到串口回馈
                    logging.warning(f"{self} 发送数据时未接收到0X66 0XBB确认回馈")

        except Exception as e:
            logging.error(f"{self}传输一帧数据时错误, 错误原因：{e}")

    """ 从设备读一帧数据    """
    def _read_bytes(self):
        try:
            if not self.isOpen():
                raise

            """ 处理bytes数据流，读取固定长度54个字节，每个帧头为0x55 0xAA 0x36  """
            ret_data = b''

            # 读取一帧数据
            # data = self.serial_obj.readline()
            data = self.serial_obj.read(size=57)
            logging.critical(f"{self} 接收到一帧数据{data}")
            # 校验帧长度、帧头、命令位、帧尾
            if len(data) != self.PACKET_LEN:
                logging.warning(f"ERROR   : {self} read frame length is not {self.PACKET_LEN}")
                raise

            if self.PACKET_HEADER != data[0:self.PACKET_HEADER_LEN]:
                logging.warning(f"WARNING : {self} read frmae without header {self.PACKET_HEADER}")
            if data[self.PACKET_HEADER_LEN:self.PACKET_HEADER_LEN+self.PACKET_CMD_LEN] in [e.value for e in mCommCmd]:
                ret_cmd_type = mCommCmd(data[self.PACKET_HEADER_LEN:self.PACKET_HEADER_LEN+self.PACKET_CMD_LEN])
            else:
                ret_cmd_type = mCommCmd.UNKNOWN
            if self.PACKET_END != data[self.PACKET_HEADER_LEN+self.PACKET_CMD_LEN+self.PACKET_DATA_LEN:]:
                logging.warning(f"WARNING : {self} read frmae without end {self.PACKET_END}")

            # 去除帧头帧尾
            ret_data = data[self.PACKET_HEADER_LEN+self.PACKET_CMD_LEN:self.PACKET_HEADER_LEN+self.PACKET_CMD_LEN+self.PACKET_DATA_LEN]
            return ret_cmd_type, ret_data

        except Exception as e:
            logging.error(f"{self}接收一帧数据发生错误，错误原因：{e}")



""" 检测端口是否存在 """
def detectPortIsExisted(port):
    # get current active com device
    if comports_device:= [comport.device for comport in serial.tools.list_ports.comports()]:
        return port in comports_device
    else:
        return False
