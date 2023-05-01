# -*- coding: utf-8 -*-
'''
Author: liuyibo 1299502716@qq.com
Date: 2023-02-15 16:44:20
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-04-30 20:56:30
FilePath: /RL_Simulation_Of_UWSNs/utils/get_time.py
Description: 获取系统时间
'''

import time
import datetime

""" 获取当前时间 """
def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

""" 获取当前时间 """
def get_current_time_apply_to_filename():
    return time.strftime('%Y_%m_%d %H_%M_%S', time.localtime(time.time()))

""" 计算时间1和时间2之间的差值，单位为s     """
def cal_diff_time_between_date1_and_date2(t1, t2):

    start = datetime.datetime.strptime(t1,"%Y-%m-%d %H:%M:%S")
    end   = datetime.datetime.strptime(t2,"%Y-%m-%d %H:%M:%S")

    return (end-start).seconds if end > start else -1


if __name__ == "__main__":
    
    date1 = get_current_time()
    time.sleep(1)
    date2 = get_current_time()
    
    date = transfer_format_from_datetime_to_date(date1, date2)
    
    print(time)