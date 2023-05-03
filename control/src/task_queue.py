#!/usr/bin/python

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import queue
from enum import Enum
from .config             import Config
from .device_manager import *
from .tool.mformatconv import *

# ! 数据库相关定义
engine          = create_engine(Config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})
session_maker   = sessionmaker(bind=engine)
session         = session_maker()
Base            = declarative_base()

class mTaskFlowDirectionEnum(Enum):
    """ task operation enum         """
    DIRECT_FILE_TO_DEVICE = 1
    DIRECT_DEVICE_TO_FILE = 2

class mTaskPriorityEnum(Enum):
    """ task queue priority enum    """
    PRIOR_LOW    = 1
    PRIOR_MEDIUM = 2
    PRIOR_HIGH   = 3

class mTask(object):
    """_summary_
    achieve task class
    Args:
        file      : file
        device    : device
        priority  : task priority
    """
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
    
class mTaskQueue(object):
    """_summary_
    achieve task queue class
    Args:
        maxsize    : task queue size
        timeout    : task queue IO timeout
    """
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

# 创建对象的基类
Base = declarative_base()

class Tasks(Base):
    """ tasks class  """
    # 创建表
    __tablename__ = "tasks"

    # 创建字段
    task_id                     = Column(Integer   , primary_key=True)    # tasks表中的id字段(主键)
    task_name                   = Column(String(64))                      # tasks表中的name字段
    task_priority               = Column(String(64))                      # tasks表中的priority字段
    source_file_id              = Column(Integer)                         # tasks表中的file_id字段
    source_file_name            = Column(String(64))                      # tasks表中的file_name字段
    source_file_size            = Column(String(64))                      # tasks表中的file_size字段
    source_file_path            = Column(String(64))                      # tasks表中的file_path字段
    target_device_id            = Column(Integer)                         # tasks表中的device_id  字段
    target_device_name          = Column(String(64))                      # tasks表中的device_name字段
    task_status                 = Column(Integer)                         # tasks表中的status        字段
    task_submit_time            = Column(String(64))                      # tasks表中的submit_time   字段
    task_submit_source          = Column(String(64))                      # tasks表中的submit_source 字段
    task_execute_time           = Column(String(64))                      # tasks表中的execute_time  字段
    task_finish_time            = Column(String(64))                      # tasks表中的finish_time   字段
    task_transfer_speed         = Column(String(64))                      # tasks表中的transfer_speed字段
    
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.task_name)
