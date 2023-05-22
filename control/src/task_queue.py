# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Author: liuyibo 1299502716@qq.com
Date: 2023-05-03 13:59:16
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-05-08 14:11:44
FilePath: \Gateway_System\control\src\task_queue.py
Description: 任务队列定义
'''
import queue
from enum import Enum
from .device_manager import *
from .tool.mformatconv import *

""" task operation enum         """
class mTaskFlowDirectionEnum(Enum):
    DIRECT_FILE_TO_DEVICE = 1
    DIRECT_DEVICE_TO_FILE = 2

""" task queue priority enum    """
class mTaskPriorityEnum(Enum):
    PRIOR_LOW    = 1
    PRIOR_MEDIUM = 2
    PRIOR_HIGH   = 3

"""_summary_
achieve task class
Args:
    file      : file
    device    : device
    priority  : task priority
"""
class mTask(object):
    def __init__(self, task_id:int, file_name: str, file_path: str, device: mDevice, direct: mTaskFlowDirectionEnum, priority: mTaskPriorityEnum):
        """ init param and create task  """
        self._task_id   = task_id
        self._file_name = file_name
        self._file_path = file_path
        self._file      = file_path + file_name

        self._device    = device
        self._direct    = direct
        self._priority  = priority

    def __repr__(self):
        return f'任务(文件{self._file} 设备{self._device} 方向{self._direct} 优先级{self._priority})'

"""_summary_
achieve task queue class
Args:
    maxsize    : task queue size
    timeout    : task queue IO timeout
"""
class mTaskQueue(object):
    def __init__(self, maxsize=10, timeout=None):
        """ init param and create queue """
        self._maxsize   = maxsize
        self._timeout   = timeout

        # create task queue
        try:
            self._queue = queue.PriorityQueue(self._maxsize)
        except Exception as e:
            print("ERROR   : Create Task Queue", e)

    def isEmpty(self):
        """ detect queue isEmpty            """
        return self._queue.empty()

    def isFull(self):
        """ detect queue isFull             """
        return self._queue.full()

    def size(self):
        """ query queue size                """
        return self._queue.qsize()

    def get(self) -> mTask:
        """ get a task from queue, block    """
        try:
            task = self._queue.get(block=True, timeout=None)
            return task[-1]
        except Exception as e:
            print("ERROR   : Read Task Queue ",e)

    def put(self, task:mTask):
        """ add a task to queue, not block  """
        try:
            self._queue.put((task._priority.value, task), block=False, timeout=self._timeout)
        except Exception as e:
            print("ERROR   : Write Task Queue ",e)

    def close(self):
        """ clear task queue                """
        self._queue.queue.clear()
