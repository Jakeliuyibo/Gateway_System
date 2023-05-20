'''
Author: liuyibo 1299502716@qq.com
Date: 2023-05-20 12:49:17
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-05-20 15:09:38
FilePath: \Gateway_System\control\src\driver\bsp_optical_fiber_comm.py
Description: 光纤通信驱动文件,基于asyncore异步封装的socket
'''
import os
import socket
import logging
import threading
import asyncore
import struct


'''
description: 实现了光纤通信驱动
'''
class mOpticalFiberCommDevice(asyncore.dispatcher):
    """ init device   """
    def __init__(self, server_interface, target_interface):
        # parse parameters
        server_interface        = server_interface.split(':')
        self.tcpserver_ip       = server_interface[0]               # 服务器IP地址
        self.tcpserver_port     = server_interface[1]               # 服务器端口号

        target_interface        = target_interface.split(':')
        self.tcpclient_ip       = target_interface[0]               # 目的服务器IP地址
        self.tcpclient_port     = target_interface[1]               # 目的服务器端口号

        # init defconfig
        self.tcpserver_obj      = None
        self.is_open            = False

    def __repr__(self):
        return '光纤通信机(端口%r 状态%r)' % (self.server_ip, self.is_open)

    """ 打开设备         """
    def open(self):
        try:
            if not detectHostIPIsExisted(self.tcpserver_ip):
                raise

            # 初始化TCP Server Socket
            asyncore.dispatcher.__init__(self)
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.bind((self.tcpserver_ip, self.tcpserver_port))

            self.is_open  = True
        except Exception as e:
            logging.error(f"ERROR   : {self} try to open failed")

    """ 关闭设备         """
    def close(self):
        try:
            self.close()
        except Exception as e:
            logging.error(f"ERROR   : {self} try to close device")

    """ 写入文件             """
    def write(self, file_path, file_name):
        
        # 1、向客户端连接TCP连接
        
        # 2、传输文件名+文件大小
        file_size = str(os.path.getsize(file_path+file_name))
        
        # 3、传输文件数据
        
        # 4、断开连接
        pass

    """ 读取文件             """
    def read(self, file_path):
        # 1、检测client_list是否为空
        
        # 2、检测是否有数据可读
        
        # 3、接收文件名+文件大小
        
        # 4、接收文件数据
        pass


    """ 子线程：监听客户端连接  """
    def listen_client(self):
        while True:
            client_sk, client_addr = self.tcpserver_obj.accept()
            self.client_list.append({client_sk, client_addr})

# import asyncore
# import struct

# class TCPDevice(asyncore.dispatcher):
#     def __init__(self, server_ip, server_port, target_ip, target_port):
#         asyncore.dispatcher.__init__(self)
#         self.create_socket()
#         self.bind((server_ip, server_port))
#         self.target_ip = target_ip
#         self.target_port = target_port
#         self.buffer = b''
        
#     def open(self):
#         pass
    
#     def close(self):
#         self.close()
    
#     def read(self):
#         data = self.recv(1024)
#         if data:
#             file_info = struct.unpack('128sI', data[:132])
#             filename = file_info[0].decode().strip('\x00')
#             filesize = file_info[1]
#             with open(filename, 'wb') as f:
#                 f.write(data[132:])
#                 remaining_bytes = filesize - len(data[132:])
#                 while remaining_bytes > 0:
#                     data = self.recv(1024)
#                     f.write(data)
#                     remaining_bytes -= len(data)
    
#     def write(self, filename):
#         with open(filename, 'rb') as f:
#             file_data = f.read()
#             file_size = len(file_data)
#             file_info = struct.pack('128sI', filename.encode(), file_size)
#             self.buffer += file_info + file_data
#             while len(self.buffer) > 0:
#                 sent = self.sendto(self.buffer, (self.target_ip, self.target_port))
#                 self.buffer = self.buffer[sent:]

# 在这个类中，我们创建了一个TCP服务器，它使用server_ip和server_port绑定到服务器。open和close函数仅用于占位符，因为在这个例子中它们不需要做任何事情。read函数从连接的客户端读取数据，并将其写入名为filename的文件中。write函数从名为filename的文件中读取数据，并将其写入到指定的target_ip和target_port。


# 请注意，在read和write函数中，我们使用了struct模块来打包和解包文件名和文件大小，以便在传输过程中传递这些信息。我们还使用了一个缓冲区来存储待发送的数据，以便在网络连接不稳定时能够处理数据的丢失和重传。与syncore模块不同，asyncore模块是异步的，因此它更适合处理大量的网络连接。同样，这个类只是一个基本示例，为了使它适合特定的应用程序，需要根据需要进行修改。



'''
description: 检测IP是否为主机地址
'''
def detectHostIPIsExisted(ip):
    hostname = socket.gethostname()
    hostip   = socket.gethostbyname(hostname)
    return ip in hostip
