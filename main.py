# -*- coding: utf-8 -*-
'''
Author: liuyibo 1299502716@qq.com
Date: 2023-04-29 21:35:29
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-05-01 13:38:19
FilePath: \Gateway_System\main.py
Description: 主函数，通过python main.py启动网关软件
'''


from multiprocessing import Process
from web.app import create_app
from control.src import init_device

'''
description: 进程：运行网关设备管理APP
'''
def create_web():
    # create flask app
    web_app = create_app("develop")

    # execute app
    web_app.run(host="localhost", port="1234", debug=False)
    
'''
description: 进程：运行网关设备控制APP
'''
def create_control():
    # init device
    init_device()
    
if __name__ == "__main__":
    # 创建driver进程
    proc_control = Process(target=create_control, args=())
    proc_control.start()
    
    # # 创建web进程
    proc_web = Process(target=create_web, args=())
    proc_web.start()
    
    proc_control.join()
    proc_web.join()