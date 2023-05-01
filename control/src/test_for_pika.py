
import pika
import threading
import multiprocessing

QUEUE_NAME = 'task_queue'

# 回调函数
def deal_task(ch, method, properties, body):
    print("received message : ", body)
    
""" 线程：监控web pika任务队列      """
def create_pika_consumer():
    # 1. 创建一个到RabbitMQ server的连接，如果连接的不是本机，
    # 则在pika.ConnectionParameters中传入具体的ip和port即可
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # 2. 创建一个channel
    channel = connection.channel()
    # 3. 创建队列，queue_declare可以使用任意次数，
    # 如果指定的queue不存在，则会创建一个queue，如果已经存在，
    # 则不会做其他动作，官方推荐，每次使用时都可以加上这句
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    # 4. 接收来自指定queue的消息
    channel.basic_consume(
        queue=QUEUE_NAME,                       # 接收指定queue的消息
        on_message_callback=deal_task,          # 接收到消息后的处理程序
        auto_ack=True)                          # 指定为True，表示消息接收到后自动给消息发送方回复确认，已收到消息
    print('[*] Waiting for message.')
    # 6. 开始循环等待，一直处于等待接收消息的状态
    channel.start_consuming()
    
if __name__ == '__main__':
    
    p = threading.Thread(target=create_pika_consumer)
    p.start()
    p.join()
    # create_pika_consumer()
    