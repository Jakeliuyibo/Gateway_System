import os, sys, time
import threading
import multiprocessing
import pika
from concurrent.futures  import ThreadPoolExecutor, ProcessPoolExecutor, wait, ALL_COMPLETED

from .config             import Config
from .utils.get_time     import cal_diff_time_between_date1_and_date2, get_current_time, get_current_time_apply_to_filename, get_current_time_with_ms_and_bias, get_current_time_with_ms
from .device_manager     import *
from .task_queue         import *
from .models.model       import *

# ! 设备列表、任务队列、处理池的定义
mdevicelist      = mDeviceList()                            # device list
mtaskqueue       = mTaskQueue(maxsize=10, timeout=3)        # task queue
mprocesspool     = ThreadPoolExecutor(10)                   # thread pool

###################################### manage device list     ###################################
###################################### manage device list     ###################################
""" 子线程：打开设备        """
def open_device_threadhandle(dev: mDevice):
    try:
        dev.open()
    except Exception as e:
        logging.error(f"ERROR   : Open Device {dev}")
    finally:
        return dev

""" 函数：修改数据库中设备信息   """
def modify_device_info_in_db():
    try:
        for dev in mdevicelist.dev_list:
            try:
                if modify_device := session.query(Device_Model).filter_by(device_id=dev.device_id).first():
                    if dev.is_Open:
                        modify_device.device_status     = 1
                        modify_device.last_work_time    = get_current_time()
                    else:
                        modify_device.device_status     = 0
                else:
                    raise
            except Exception as e:
                logging.error(f"未在数据库中找到{dev}信息, 错误原因{e}")
    except Exception as e:
        logging.error(f"修改设备信息对应的数据库信息, 错误原因{e}")
    finally:
        # 提交数据库修改
        session.commit()

""" 线程：初始化设备列表        """
def init_device_list_threadhandle():
    # load device from db
    dev_list = load_device_from_db()

    tt_pool = ThreadPoolExecutor(10)
    tt_list = []
    for dev in dev_list:
        #open device and get fd handle
        tt_list.append(tt_pool.submit(open_device_threadhandle, dev))

    # wait thread pool end...
    wait(tt_list, return_when=ALL_COMPLETED)

    # append device to device_list
    for tt in tt_list:
        if tt.result():
            mdevicelist.add(tt.result())

    logging.critical(f"完成设备列表初始化，存在{mdevicelist.size()}个设备")
    modify_device_info_in_db()

""" 多线程：监控设备数据IO      """
def monitor_device_threadhandle(dev: mDevice):
    while dev.is_Open:
        if dev.isReadable():
            task_file_path              = dev.storage_filepath
            task_submit_time            = get_current_time_with_ms()
            task_name                   = f"task device{dev.device_id}-file{get_current_time_apply_to_filename()}"

            # 创建数据库记录
            add_task                    = Task_Model()
            add_task.target_device_id   = dev.device_id
            add_task.target_device_name = dev.device_name
            add_task.source_file_path   = task_file_path
            add_task.task_name          = task_name
            add_task.task_priority      = "0"
            add_task.task_status        = "schedule"                    # success\pending\queue\schedule\fail
            add_task.task_submit_time   = task_submit_time
            add_task.task_submit_source = "recv"
            session.add(add_task)
            session.commit()

            # 提交任务
            mtaskqueue.put(mTask(add_task.task_id, "", task_file_path,
                                    dev,
                                    mTaskFlowDirectionEnum.DIRECT_DEVICE_TO_FILE,
                                    mTaskPriorityEnum.PRIOR_LOW))
        time.sleep(0.1)

###################################### deal data forwarding ######################################
###################################### deal data forwarding ######################################
""" 线程池中线程：处理任务    """
def deal_data_forwarding_processhandle(args):
    # 处理参数
    task = args[0]

    # 处理任务
    if task._direct == mTaskFlowDirectionEnum.DIRECT_DEVICE_TO_FILE:          # device to file
        try:
            execute_time    = get_current_time_with_ms()
            file_name       = task._device.read(task._file_path)
            if file_name:
                file_size       = str(os.path.getsize(task._file_path+file_name))

                # todo
                # ! 水声通信机的完成速率-1
                if task._device.device_name  == "underwater acoustic comm module":
                    finish_time     = get_current_time_with_ms_and_bias(1)
                else:
                    finish_time     = get_current_time_with_ms()

                transfer_speed  = str(round(float(file_size) / float(cal_diff_time_between_date1_and_date2(execute_time, finish_time)),2))

                return {"task_id"       :task._task_id,
                        "flag"          :"success",
                        "direct"        :"DIRECT_DEVICE_TO_FILE",
                        "file_name"     :file_name,
                        "file_size"     :file_size,
                        "execute_time"  :execute_time,
                        "finish_time"   :finish_time,
                        "transfer_speed":transfer_speed}
            else:
                raise
        except Exception as e:
            logging.error(f"ERROR   : 线程池处理DIRECT_DEVICE_TO_FILE任务{task._task_id}")
            return     {"task_id"       :task._task_id,
                        "flag"          :"fail",
                        "direct"        :"DIRECT_DEVICE_TO_FILE"}
    elif task._direct == mTaskFlowDirectionEnum.DIRECT_FILE_TO_DEVICE:        # file to device
        try:
            execute_time    = get_current_time_with_ms()
            file_size       = task._device.write(task._file_path, task._file_name)
            if file_size != -1:
                finish_time     = get_current_time_with_ms()

                # todo
                # ! 水声通信机的完成速率-1
                if task._device.device_name  == "underwater acoustic comm module":
                    finish_time     = get_current_time_with_ms_and_bias(2)
                else:
                    finish_time     = get_current_time_with_ms()

                transfer_speed  = str(round(float(file_size) / float(cal_diff_time_between_date1_and_date2(execute_time, finish_time)),2))

                return {"task_id"       :task._task_id,
                        "flag"          :"success",
                        "direct"        :"DIRECT_FILE_TO_DEVICE",
                        "execute_time"  :execute_time,
                        "finish_time"   :finish_time,
                        "transfer_speed":transfer_speed}
            else:
                raise
        except Exception as e:
            logging.error(f"ERROR   : 线程池处理DIRECT_FILE_TO_DEVICE任务{task._task_id}")
            return {"task_id"       :task._task_id,
                    "flag"          :"fail",
                    "direct"        :"DIRECT_FILE_TO_DEVICE"}

""" 回调函数：任务处理完成  """
def deal_data_forwarding_callback(res):
    task        = res.result()
    task_id     = task.get('task_id')
    task_flag   = task.get('flag')
    task_direct = task.get('direct')

    # 将任务处理结果（时间、任务状态）写入数据库
    try:
        modify_task = session.query(Task_Model).filter_by(task_id=task_id).first()
        if modify_task:
            if task_flag == "success":
                modify_task.task_status         = "success"
                modify_task.task_execute_time   = task.get('execute_time')
                modify_task.task_finish_time    = task.get('finish_time')
                modify_task.task_transfer_speed = task.get('transfer_speed')
                if task_direct == "DIRECT_DEVICE_TO_FILE":
                    modify_task.source_file_name    = task.get('file_name')
                    modify_task.source_file_size    = task.get('file_size')
                    logging.critical(f"线程池回调 ： 完成DIRECT_DEVICE_TO_FILE任务{task_id}")
                else:
                    logging.critical(f"线程池回调 ： 完成DIRECT_FILE_TO_DEVICE任务{task_id}")
            else:
                modify_task.task_status             = "fail"
                logging.critical(f"线程池回调 ： 执行任务{task_id}失败")

            # 提交数据库修改
            session.commit()
        else:
            raise
    except Exception as e:
        logging.error(f"线程池处理任务{task_id}回调出现错误, 错误原因{e}")

""" 线程：监控任务队列      """
def monitor_task_queue_threadhandle():
    while True:
        # block wait task from task queue
        submit_task = mtaskqueue.get()

        # submit task to processpool
        fur = mprocesspool.submit(deal_data_forwarding_processhandle, args=(submit_task,))

        # set callback function
        fur.add_done_callback(deal_data_forwarding_callback)

###################################### deal web task        ######################################
###################################### deal web task        ######################################
""" 回调函数：处理来自web的任务     """
def deal_web_task_request_callback(ch, method, properties, body):
    # 解析来自web服务器的任务请求
    web_task    = eval(body)
    task_id     = web_task.get("task_id")
    file_name   = web_task.get("file_name")
    file_path   = web_task.get("file_path")
    device_id   = int(web_task.get("device_id"))
    direct      = mTaskFlowDirectionEnum[web_task.get("direct")]
    priority    = mTaskPriorityEnum[web_task.get("priority")]

    # TODO 搜索设备
    device = mdevicelist.query(device_id)
    if device:
        # 创建任务并发布任务
        mtaskqueue.put(mTask(task_id, file_name, file_path, device, direct, priority))
    else:
        logging.error(f"ERROR   : 未查询到web请求对应的设备{device_id}")

""" 线程：监控web pika任务队列      """
def monitor_web_task_threadhandle():
    """ 创建RabbitMQ的消费者队列    """
    # 1. 创建RabbitMQ server的连接
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', '5672'))

    # 2. 创建一个channel
    channel = connection.channel()

    # 3. 创建队列，queue_declare可以使用任意次数，
    channel.queue_declare(queue=Config.PIKA_TASKQUEUE_NAME, durable=True)

    # 4. 接收来自指定queue的消息
    # auto_ack指定为True，表示消息接收到后自动给消息发送方回复确认，已收到消息
    channel.basic_consume(
        queue=Config.PIKA_TASKQUEUE_NAME,
        on_message_callback=deal_web_task_request_callback,
        auto_ack=True)

    logging.warning('SUCCESS : Create Pika server.')

    # 6. 开始循环等待，一直处于等待接收消息的状态
    channel.start_consuming()

###################################### core scheduling      ######################################
###################################### core scheduling      ######################################

def test_for_core_scheduling():
    """ 初始化设备列表和任务队列          """
    # create threading : init device list
    t1 = threading.Thread(target=init_device_list_threadhandle  , name="init device list" , args=())
    t1.start()
    t1.join()

    # create threading : manage task queue
    t2 = threading.Thread(target=monitor_task_queue_threadhandle, name="manage task queue", args=())
    t2.start()

    """ 监控web请求                     """
    # create threading : monitor pika queue
    t3 = threading.Thread(target=monitor_web_task_threadhandle  , name="monitor web task" , args=())
    t3.start()

    """ 监控设备请求                    """
    # create threading : monitor device list
    tt_list = []
    for dev in mdevicelist.dev_list:
        tt = threading.Thread(target=monitor_device_threadhandle     , name="monitor device list"    , args=(dev, ))
        tt.start()
        tt_list.append(tt)

    for tt in tt_list:
        tt.join()

    # close
    mprocesspool.shutdown()
    mtaskqueue.close()
    mdevicelist.close()
    session.close()

if __name__ == "__main__":
    test_for_core_scheduling()