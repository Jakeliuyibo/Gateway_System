# -*- coding: utf-8 -*-

from multiprocessing import Process
from test import *
import logging

if __name__ == "__main__":
    logging.info("app start...")
    
    # 创建driver进程
    proc_control = Process(target=create_control, args=())
    proc_control.start()
    
    # # 创建web进程
    proc_web = Process(target=create_web, args=())
    proc_web.start()
    
    proc_control.join()
    proc_web.join()

    logging.critical("app end...")