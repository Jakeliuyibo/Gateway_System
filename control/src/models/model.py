# -*- coding: utf-8 -*-
'''
Author: liuyibo 1299502716@qq.com
Date: 2023-05-08 14:10:45
LastEditors: liuyibo 1299502716@qq.com
LastEditTime: 2023-05-08 14:18:06
FilePath: \Gateway_System\control\src\model.py
Description: 数据库相关模型定义
'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..config             import Config

# ! 数据库相关定义
engine          = create_engine(Config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})
session_maker   = sessionmaker(bind=engine)
session         = session_maker()
Base            = declarative_base()    # 创建对象的基类

""" device class  """
class Device_Model(Base):
    # 创建表
    __tablename__ = "devices"

    # 创建字段
    device_id                   = Column(Integer   , primary_key=True)              # devices表中的id字段(主键)
    device_name                 = Column(String(64), nullable=False, index=True)    # devices表中的name字段
    device_type                 = Column(String(64), nullable=False, index=True)    # devices表中的type字段
    device_status               = Column(String(64), nullable=False, index=True)    # devices表中的status字段
    device_property             = Column(String(64), nullable=False, index=True)    # devices表中的property字段
    device_description          = Column(String(64), nullable=False, index=True)    # devices表中的description字段
    last_work_time              = Column(String(64), nullable=False, index=True)    # devices表中的last_work_time字段
    last_edit_time              = Column(String(64), nullable=False, index=True)    # devices表中的last_edit_time字段
    
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.device_name)
    
""" tasks class  """
class Task_Model(Base):
    # 创建表
    __tablename__ = "tasks"

    # 创建字段
    task_id                     = Column(Integer   , primary_key=True)              # tasks表中的id字段(主键)
    task_name                   = Column(String(64))                                # tasks表中的name          字段
    task_priority               = Column(String(64))                                # tasks表中的priority      字段
    source_file_id              = Column(Integer)                                   # tasks表中的file_id       字段
    source_file_name            = Column(String(64))                                # tasks表中的file_name     字段
    source_file_size            = Column(String(64))                                # tasks表中的file_size     字段
    source_file_path            = Column(String(64))                                # tasks表中的file_path     字段
    target_device_id            = Column(Integer)                                   # tasks表中的device_id     字段
    target_device_name          = Column(String(64))                                # tasks表中的device_name   字段
    task_status                 = Column(Integer)                                   # tasks表中的status        字段
    task_submit_time            = Column(String(64))                                # tasks表中的submit_time   字段
    task_submit_source          = Column(String(64))                                # tasks表中的submit_source 字段
    task_execute_time           = Column(String(64))                                # tasks表中的execute_time  字段
    task_finish_time            = Column(String(64))                                # tasks表中的finish_time   字段
    task_transfer_speed         = Column(String(64))                                # tasks表中的transfer_speed字段
    
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.task_name)