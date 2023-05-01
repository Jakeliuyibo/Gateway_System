# -*- coding: utf-8 -*-

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
