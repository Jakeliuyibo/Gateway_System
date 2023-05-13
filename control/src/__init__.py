# -*- coding: utf-8 -*-

import logging
from control.src.core_scheduling import test_for_core_scheduling
from .utils.mlogging import logs_init
from .config import Config


'''
description: 初始化设备
'''
def init_device():

    # init logging
    if Config.LOGGING_CONFIG_ABLE:
        logs_init(Config)

    logging.critical("初始化网关设备驱动 start...")

    test_for_core_scheduling()

    logging.error("网关设备驱动异常 end...")