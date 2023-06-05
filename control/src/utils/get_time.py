# -*- coding: utf-8 -*-
'''
Author: liuyibo 1299502716@qq.com
Date: 2023-02-15 16:44:20
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-06-05 13:36:49
FilePath: /RL_Simulation_Of_UWSNs/utils/get_time.py
Description: 获取系统时间
'''

import time
import datetime

""" 获取当前时间 """
def get_current_time():
    # return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # 将当前时间戳转换为datetime对象
    dt = datetime.datetime.fromtimestamp(time.time())

    # 将datetime对象格式化为指定格式的字符串
    return dt.strftime('%Y-%m-%d %H:%M:%S.%f')

""" 获取当前时间 """
def get_current_time_apply_to_filename():
    return time.strftime('%Y_%m_%d %H_%M_%S', time.localtime(time.time()))

""" 计算时间1和时间2之间的差值，单位为s     """
def cal_diff_time_between_date1_and_date2(t1, t2):

    start = datetime.datetime.strptime(t1,"%Y-%m-%d %H:%M:%S.%f")
    end   = datetime.datetime.strptime(t2,"%Y-%m-%d %H:%M:%S.%f")

    return (end-start).seconds + (end-start).microseconds/1000000 if end > start else -1

""" 获取当前时间 """
def get_current_time_with_bias(bias):
    dt = datetime.datetime.fromtimestamp(time.time())  - datetime.timedelta(seconds=bias)
    return dt.strftime('%Y-%m-%d %H:%M:%S.%f')
