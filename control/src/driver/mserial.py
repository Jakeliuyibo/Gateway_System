#!/usr/bin/python

import logging
import os, time
import serial
import serial.tools.list_ports

"""_summary_
achieve serial class
Args:
    port             : port name
    baudrate         : port baud rate
    timeout          : port configure and IO out-time , if time=0 : no wait, else wait (time) seconds
"""
class mSerial(object):
    """ init mSerial class  """
    def __init__(self, port, baudrate=115200, timeout=1):
        # set params
        self.scom_port      = port
        self.scom_baudrate  = baudrate
        self.scom_timeout   = timeout
        
        # try to open scom interface
        try:
            if detectPortIsExisted(port):
                self.scom_obj   = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
                self.flagState  = True
            else:
                raise
        except Exception as e:
            self.scom_obj       = None
            self.flagState      = False
            logging.error(f"ERROR   : {self} try to init ")

    def __repr__(self):
        return '串口(端口%r 状态%r)' % (self.scom_port, self.flagState)
    
    """ detect the serial open status         """
    def isOpen(self):
        return self.flagState
    
    """ detect the serial is readable         """
    def isReadable(self):
        return self.scom_obj.inWaiting() != 0
    
    """ read bytes data from serial           """
    def read(self):
        try:
            if self.isOpen():
                count = self.scom_obj.inWaiting()
                if count != 0:
                    return self.scom_obj.read(count)
                else:
                    return None
            else:
                raise
        except Exception as e:
            print(f"ERROR   : {self} try to read data, err-{e}")
            
    """ read bytes data from serial           """
    def read_size(self, size):
        try:
            if self.isOpen():
                return self.scom_obj.read(size)
            else:
                raise
        except Exception as e:
            print(f"ERROR   : {self} try to read data, err-{e}")
            
    """ read bytes data until expected char    """
    def readuntil(self, expc):
        try:
            if self.isOpen():
                read_data = self.scom_obj.read_until(expected=expc)
                if read_data:
                    return read_data
                else:
                    raise RuntimeError
            else:
                raise ModuleNotFoundError
        except Exception as e:
            print(f"ERROR   : {self} try to read data until expc char, but timeout, err-{e}")
            
    """ write bytes data to serial    """
    def write(self, data):
        try:
            if self.isOpen() and len(data) != 0:
                self.scom_obj.write(data)
        except Exception as e:
            print(f"ERROR   : {self} try to write dato, err-{e}")
    
    """ close serial            """
    def close(self):
        try:
            if self.isOpen():
                self.scom_obj.close()
                self.flagState = False
            else:
                raise
        except Exception as e:
            print("ERROR   : Close serial")

""" 检测端口是否存在 """
def detectPortIsExisted(port):
    # get current active com device
    if comports_device:= [comport.device for comport in serial.tools.list_ports.comports()]:
        return port in comports_device
    else:
        return False