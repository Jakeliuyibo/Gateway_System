'''
Author: liuyibo 1299502716@qq.com
Date: 2023-05-08 15:50:48
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-06-26 21:27:26
FilePath: \Gateway_System\control\src\driver\bsp_satellite_comm.py
Description: 天通通信驱动文件
'''

import os
import socket
import logging
import threading
import struct
import random
from ..utils.get_time import get_current_time_apply_to_filename
from .msocket import *

class mSatelliteCommBase(object):
    FILE_NAME_LEN               = 32                             # 传输的文件名长度
    FILE_SIZE_LEN               = 8                              # 传输的文件大小长度
    FILE_INFO_LEN               = FILE_NAME_LEN + FILE_SIZE_LEN  # 传输的文件信息长度
    FILE_NAME_STRIP             = '\x00'                         # 传输文件名末位填充符

'''
description: 实现了天基通信驱动
'''
class mSatelliteCommDevice(mSatelliteCommBase):
    """ init device   """
    def __init__(self, local_ip , local_port, target_ip, target_port):
        # parse parameters
        self.local_ip           = local_ip              # 本地服务器IP地址
        self.local_port         = local_port            # 本地服务器端口号
        self.target_ip          = target_ip             # 目的服务器IP地址
        self.target_port        = target_port           # 目的服务器端口号

        # init defconfig
        self.localserver_obj    = None
        self.recv_buf           = b''                   # 读取缓存
        self.is_open            = False

    def __repr__(self):
        return '天基通信(状态%r)' % (self.is_open)

    """ 检测设备是否在线  """
    def isOpen(self):
        return self.is_open

    """ 打开设备    """
    def open(self):
        try:
            if not detectHostIPIsExisted(self.local_ip):
                raise

            # 初始化本地服务器
            self.localserver_obj    = TcpServer(self.local_ip, self.local_port)
            self.is_open            = True
        except Exception as e:
            logging.info(f"ERROR   : {self} try to open failed, {e}")

    """ 关闭设备    """
    def close(self):
        try:
            self.localserver_obj.close()
            self.is_open            = False
        except Exception as e:
            logging.info(f"ERROR   : {self} try to close device")

    """ 检测tcp服务器是否有数据可读 """
    def isReadable(self):
        return self.localserver_obj.size() > self.FILE_INFO_LEN and len(self.recv_buf)==0

    """ 从设备读取文件             """
    def read(self, file_path):
        try:
            if not self.isReadable():
                raise

            try:
                # 读取数据并存入缓存
                data = self.localserver_obj.read_from_buf()
                if data:
                    self.recv_buf += data

                    if len(self.recv_buf) < self.FILE_INFO_LEN:
                        logging.error(f"{self}读取数据长度不足self.FILE_INFO_LEN")
                        return None
                    else:
                        # 解析文件名+文件大小
                        file_name, file_size = struct.unpack('%dsQ'%(self.FILE_NAME_LEN), self.recv_buf[:self.FILE_INFO_LEN])
                        file_name = file_name.decode('utf-8').rstrip(self.FILE_NAME_STRIP)
                        # 死循环读取直到长度大于等于file_size+self.FILE_INFO_LEN
                        while len(self.recv_buf) < file_size + self.FILE_INFO_LEN:
                            data = self.localserver_obj.read_from_buf()
                            if data:
                                self.recv_buf += data
                            time.sleep(1)

                        # 解析文件数据
                        file_data = self.recv_buf[self.FILE_INFO_LEN: self.FILE_INFO_LEN+file_size]
                        # 删除缓存中的数据
                        self.recv_buf = self.recv_buf[self.FILE_INFO_LEN + file_size:]

                        # 写入文件并返回文件名
                        recv_name = f'{file_name}.REC_{get_current_time_apply_to_filename()}'
                        with open(file_path+recv_name, 'wb') as f:
                            f.write(file_data)
                        logging.critical(f"{self}接收到客户端传输的文件{file_name}")

                        # 延迟
                        time.sleep(2.35+0.1*random.randint(0,100)/100)

                        return recv_name
                else:
                    raise
            except Exception as e:
                logging.error(f"{self}读取数据为空：{e}")
                return None
        except Exception as e :
            logging.error(f"{self}没有数据可读：{e}")
            return None

    """ 向设备写入文件    """
    def write(self, file_path, file_name):
        try:
            # 检测文件是否存在
            if not os.path.exists(file_path+file_name):
                raise

            try:
                # 建立TCP客户端
                client = TcpClient(self.target_ip, self.target_port)

                # 构建包=文件名称+文件大小+文件数据
                file_size = os.path.getsize(file_path+file_name)
                with open(file_path+file_name, "rb") as file_obj:
                    file_data = file_obj.read()
                package = struct.pack('%dsQ'%(self.FILE_NAME_LEN), file_name.encode('utf-8'), file_size) + file_data

                # 向目标服务器发送数据
                client.send_to_server(package)
                client.close()

                # 延迟
                time.sleep(2.38+0.1*random.randint(0,100)/100)

                return file_size
            except Exception as e:
                logging.error(f"{self}写入文件时{file_path+file_name}错误")
                return -1
        except Exception as e:
            logging.error(f"{self}写入的文件{file_path+file_name}不存在")
            return -1
