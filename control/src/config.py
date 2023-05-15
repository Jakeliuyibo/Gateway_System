# -*- coding: utf-8 -*-
'''
Author: liuyibo 1299502716@qq.com
Date: 2023-04-29 22:20:06
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-05-03 16:15:29
FilePath: \Gateway_System\config.py
Description: 全局配置
'''
import os
import logging
import platform
from .utils.get_time import get_current_time_apply_to_filename

'''
description: 配置
'''
class Config(object):
    # 调试模式配置
    DEBUG = True

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/db/gateway.db"

    LOGGING_CONFIG_ABLE          = True
    LOGGING_FILE_PATH            = f'logs/device/{get_current_time_apply_to_filename()}.log'    # 设置logging文件输出路径
    LOGGING_FILE_HANDLER_LEVEL   = logging.WARNING                                              # 设置logging文件输出等级
    LOGGING_STREAM_HANDLER_LEVEL = logging.WARNING                                              # 设置logging终端输出等级
    LOGGING_FILE_FORMAT          = logging.Formatter('%(asctime)s - %(filename)s:%(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    LOGGING_STREAM_FORMAT        = logging.Formatter('%(message)s')

    # 操作系统
    OS_SYSTEM = platform.system()
    if OS_SYSTEM == 'Windows':      # ! Windows
        # pika任务队列名称
        PIKA_TASKQUEUE_NAME          = 'web_task_queue_for_windows'
    else:                           # ! Linux
        # pika任务队列名称
        PIKA_TASKQUEUE_NAME          = 'web_task_queue_for_linux'