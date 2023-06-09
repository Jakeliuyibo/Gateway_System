'''
Author: liuyibo 1299502716@qq.com
Date: 2023-05-20 21:49:00
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-05-22 19:14:32
FilePath: \Gateway_System\control\src\driver\msocket.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 导入socket模块
import socket
import threading
import logging
import time
import select

class TcpBase(object):
    TCP_TRANS_SIZE = 4 * 1024 * 1024           # TCP传输缓冲区大小

'''
description: 阻塞的Tcp服务器类
'''
class TcpServer(TcpBase):
    # 初始化函数，根据传入的主机地址和端口构建TCP服务器
    def __init__(self, host, port):
        # 设置参数
        self.host = host
        self.port = port

        # 创建TCP Socket Server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(1)

        self.buf_lock  = threading.Lock()
        self.read_from_client_buf = b''

        # 子线程接收客户端请求
        th = threading.Thread(target=self.accept_client, args=())
        th.start()

    def __repr__(self):
        return f"TCP服务器{self.host}:{self.port}"

    """ 子线程：接收客户端请求的函数 """
    def accept_client(self):
        # 等待客户端连接
        while True:
            client, addr = self.server.accept()
            logging.warning(f"{self}接收到客户端{addr}连接")

            # 创建子线程去阻塞等待客户端数据
            th = threading.Thread(target=self.recv_from_client, args=(client, addr))
            th.start()

    """ 接收客户端数据的函数         """
    def recv_from_client(self, client, addr):
        # 阻塞等待客户端数据
        while True:
            if data:= client.recv(self.TCP_TRANS_SIZE):
                # 写入数据缓存
                self.write_to_buf(data)
            else:
                # 如果接收到的数据为空，说明客户端已断开连接
                client.close()
                break

    """ 写入数据缓存read_from_client_buf    """
    def write_to_buf(self, data):
        with self.buf_lock:
            self.read_from_client_buf += data

    """ 从缓存read_from_client_buf读取数据  """
    def read_from_buf(self):
        with self.buf_lock:
            ret = self.read_from_client_buf
            self.read_from_client_buf = b''
        return ret

    """ 检测是否有数据可读                  """
    def readable(self):
        with self.buf_lock:
            ret = len(self.read_from_client_buf) > 0
        return ret

    """ 检测缓存read_from_client_buf可读数据大小    """
    def size(self):
        with self.buf_lock:
            ret = len(self.read_from_client_buf)
        return ret

    """ 关闭服务器                         """
    def close(self):
        self.server.close()

'''
description: 基于阻塞的TCP客户端
'''
class TcpClient(TcpBase):
    def __init__(self, host, port):
        try:
            # 创建TCP客户端连接
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((host, port))
            self.is_Connected = True
            logging.warning(f"{self}成功连接至服务器{host}:{port}")
        except Exception as e:
            self.is_Connected = False
            logging.error(f"{self}连接服务器{host}:{port}失败，{e}")

    def __repr__(self):
        return "客户端"

    """ 发送数据给服务器    """
    def send_to_server(self, data):
        try:
            if not self.is_Connected:
                raise

            # 发送数据，每个包长self.TCP_TRANS_SIZE
            while data:
                sent = self.client.send(data[:self.TCP_TRANS_SIZE])
                data = data[sent:]
        except Exception as e:
            self.close()
            logging.error(f"{self}向服务器发送数据失败，未建立连接，{e}")

    """ 关闭客户端连接      """
    def close(self):
        try:
            if not self.is_Connected:
                raise

            self.client.close()
        except Exception as e:
            logging.error(f"异常关闭{self}连接，{e}")
        finally:
            self.is_Connected = False


'''
description: 基于Select多路复用的Tcp服务器类
'''
class TcpServer_Multiplexing(TcpBase):
    # 初始化函数，根据传入的主机地址和端口构建TCP服务器
    def __init__(self, host, port):
        # 设置参数
        self.host = host
        self.port = port

        # 创建TCP Socket Server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(128)

        # 多路复用监听的文件描述符
        self.connections    = [self.server]
        self.buf_lock       = threading.Lock()
        self.read_from_client_buf = {}

        # 子线程接收客户端请求
        th = threading.Thread(target=self.handle_select, args=())
        th.start()

    def __repr__(self):
        return f"TCP服务器{self.host}:{self.port}"

    """ 子线程：处理IO多路复用 """
    def handle_select(self):
        while True:
            rlist, _, _ = select.select(self.connections, [], [])
            for sock in rlist:
                if sock == self.server:
                    client_sock, client_addr = sock.accept()
                    logging.warning(f"{self}接收到客户端{client_addr}连接")
                    client_sock.setblocking(False)
                    self.connections.append(client_sock)
                else:
                    try:
                        data = sock.recv(self.TCP_TRANS_SIZE)
                        if data:
                            self.write_to_buf(sock, data)
                        else:
                            sock.close()
                            self.connections.remove(sock)
                    except socket.error:
                        sock.close()
                        self.connections.remove(sock)
                        del self.read_from_client_buf[sock]

    """ 写入数据缓存read_from_client_buf    """
    def write_to_buf(self, sock, data):
        with self.buf_lock:
            if sock not in self.read_from_client_buf:
                self.read_from_client_buf[sock] = b''
            self.read_from_client_buf[sock] += data

    """ 从缓存read_from_client_buf读取数据  """
    def read_from_buf(self, sock):
        with self.buf_lock:
            ret = self.read_from_client_buf[sock]
            self.read_from_client_buf[sock] = b''
        return ret

    """ 检测是否有数据可读                  """
    def readable(self, min_length):
        with self.buf_lock:
            for sock in self.read_from_client_buf:
                if len(self.read_from_client_buf[sock]) >= min_length:
                    return True, sock
        return False, None

    """ 关闭服务器                         """
    def close(self):
        self.server.close()


'''
description: 检测IP是否为主机地址
'''
from netifaces import interfaces, ifaddresses, AF_INET
def detectHostIPIsExisted(ip):
    localIP_list = []
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        localIP_list.append(addresses[0])

    return ip in localIP_list
