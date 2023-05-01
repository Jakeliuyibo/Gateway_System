import os, sys, time
import threading
import queue
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, ALL_COMPLETED

from device_manager     import *
from forwarding_rule    import *
from task_queue         import *

mdevicelist      = mDeviceList(maxsize=10)                  # device list
mruletable       = mRuleTable(maxsize=10)                   # rule table
mtaskqueue       = mTaskQueue(maxsize=10, timeout=3)        # task queue
mdealprocesspool = ProcessPoolExecutor(10)                  # process pool

submit_task      = None                                     # shared submit task

###################################### manage device list     ###################################
###################################### manage device list     ###################################
""" 子线程：打开设备        """
def open_device_threadhandle(device: mDevice):
    try:
        device.open()
    except Exception as e:
        print("ERROR   : Open Device", device._device)
    finally:
        return device

""" 线程：初始化设备列表        """
def init_device_list_threadhandle(file_name):
    global mdevicelist

    # load device from "./config/device.conf"
    dev_list = load_device_from_config_file(file_name)
    
    tt_pool = ThreadPoolExecutor(10)
    tt_list = []
    for dev in dev_list:
        #open device and get fd handle
        tt_list.append(tt_pool.submit(open_device_threadhandle, dev))

    # wait thread pool end...
    wait(tt_list, return_when=ALL_COMPLETED)

    # append device to device_list
    for tt in tt_list:
        mdevicelist.add(tt.result())
        
""" 多线程：监控设备数据IO      """
def monitor_device_threadhandle(dev: mDevice):
    while True:
        if dev.isReadable():
            print("serial is readable")
            task_file   = dev._storage_filename + get_localtime_str_by_second()
            print("create task file", task_file)
            task_device = dev
            task_direct = mTaskFlowDirectionEnum.DIRECT_DEVICE_TO_FILE
            task_prior  = mTaskPriorityEnum.PRIOR_LOW
            mtaskqueue.put(mTask(file=task_file, device=task_device, direct=task_direct, priority=task_prior))
        time.sleep(1)

###################################### manage forwarding rule ###################################
###################################### manage forwarding rule ###################################
""" 线程：初始化转发规则    """
def init_forwarding_rule_threadhandle(file_name):
    global mruletable

    rule_list = load_rule_table_from_config_file(file_name)
    for rule in rule_list:
        mruletable.add(rule)

###################################### deal data forwarding ######################################
###################################### deal data forwarding ######################################
""" 进程池中进程：处理任务    """
def deal_data_forwarding_processhandle(args):
    global submit_task

    # print("args", args)
    # print("args type", type(args))
    try:
        # get task ptr
        cur_task    = submit_task
        print("process  pool task", os.getpid(), "file=", cur_task._file, "device=", cur_task._device._identify)
        cur_direct  = cur_task._direct
        if cur_direct == mTaskFlowDirectionEnum.DIRECT_DEVICE_TO_FILE:          # device to file
            print("DIRECT_DEVICE_TO_FILE")
            with open(cur_task._file, "w", encoding="utf-8") as obj_file:
                rdata = cur_task._device.read()
                if rdata:
                    print("rdata", rdata)
                    obj_file.write(rdata)
        elif cur_direct == mTaskFlowDirectionEnum.DIRECT_FILE_TO_DEVICE:        # file to device
            print("DIRECT_FILE_TO_DEVICE")
            with open(cur_task._file, "r", encoding="utf-8") as obj_file:
                cur_task._outdevice.write(obj_file.read())
        return "ok"
    except Exception as e:
        print("error", e)
        print("ERROR   : Deal data forwarding process ", os.getpid(), "file=", cur_task._file, "device=", cur_task._device._identify)
        return "fail"

""" 回调函数：任务处理完成  """
def deal_data_forwarding_callback(res):
    ret = res.result()
    logging.info("SUCCESS  : Deal data forwarding callback ", res.result())

""" 线程：监控任务队列      """
def monitor_task_queue_threadhandle():
    global mtaskqueue
    global submit_task
    global mdealprocesspool

    while True:
        # block wait task from task queue
        submit_task = mtaskqueue.get()

        # submit task to processpool
        fur = mdealprocesspool.submit(deal_data_forwarding_processhandle, args=())

        # set callback function
        fur.add_done_callback(deal_data_forwarding_callback)

###################################### core scheduling      ######################################
###################################### core scheduling      ######################################

def test_for_core_scheduling():
    """ 初始化设备列表和转发规则列表    """
    # create threading : init device list
    t1 = threading.Thread(target=init_device_list_threadhandle     , name="init device list"    , args=("../config/device.conf", ))
    t1.start()

    # create threading : init forwarding rule
    t2 = threading.Thread(target=init_forwarding_rule_threadhandle , name="init forwarding rule", args=("../config/forwarding_rule.conf", ))
    t2.start()

    t1.join()
    t2.join()

    # create threading : manage task queue
    t3 = threading.Thread(target=monitor_task_queue_threadhandle    , name="manage task queue"     , args=())
    t3.start()

    """ 监控设备请求                    """
    # create threading : monitor device list
    for dev in mdevicelist._list:
        tt = threading.Thread(target=monitor_device_threadhandle     , name="monitor device list"    , args=(dev, ))
        tt.start()

    # wait keyboard input : add add1 end
    while True:
        keyin = input()
        # if keyin == "add1":
        #     mtaskqueue.put(mTask("../data/TMP_SATELLITE2022_11_14_18_17_25", mdevicelist._list[0], mTaskFlowDirectionEnum.DIRECT_FILE_TO_DEVICE, mTaskPriorityEnum.PRIOR_LOW))
        # elif keyin == "add2":
        #     mtaskqueue.put(mTask("../data/TMP_test", mdevicelist._list[0], mTaskFlowDirectionEnum.DIRECT_DEVICE_TO_FILE, mTaskPriorityEnum.PRIOR_LOW))

        if keyin == "end":
            print("recv end")
            break


    # try:
    #     if mdevicelist._list[0]._obj_dev.isWork():
    #         print("device ok")
    #     else:
    #         raise
    # except Exception as e:
    #     print("try error ", e)

    # t4 = threading.Thread(target=thread_read_data)
    # t4.start()

    # # wait keyboard input : end
    # while True:
    #     mdevicelist._list[0].write("hello\r\n")
    #     time.sleep(5)

    # close
    mdealprocesspool.shutdown()
    mtaskqueue.close()
    mruletable.close()
    mdevicelist.close()

if __name__ == "__main__":
    test_for_core_scheduling()