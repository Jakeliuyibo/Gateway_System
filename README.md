# Gateway System

## Brief:
    The gateway system consists of two intergrated software, one is control software, the other is management software.

    The control software is based on multi-threading for data access to the device, the device mainly include serial
    port devices and TCP/IP-based network devices. When reading and writing files on a serial port device, you should
    pay attention to the data format (start bit, cmd bit, and end bit), ACK mechanism,
    and retransmission mechanism (to be implemented).

    The management software is developed using the AMIS framework of Baidu open-source and Flask Web framework. The
    front-end uses JSON for the configuration interface, and the back-end uses the default HTTP server of Flask to
    build responses. blueprint, session, sql(redis, sqlite) and other technologies are used to implement logical
    functions such as user login, device viewing, device editing, history viewing, and task submission.

    To communicate between the two separate processes, the control and management software, we use the RabbitMQ-based
    pika module, which uses message queues to exchange data.

## Usage method:
    Install pyhton, flask, redis, sqlite, pika, related to environment (pip install -r requirements.txt), and then
    use the terminal to run the main program (python main.py), use the browser to access 127.0.0.1 + port number,
    you can access to the local Web!

## Directory structure:
- Gateway System
- control  : device communication module driver file
- db       : database
- logs     : log files
- storage  : received files and uploaded files
- web      : web applicaton based on Flask

![登录界面](https://user-images.githubusercontent.com/49876032/221079815-56105437-96dd-438b-af9a-f8976a88845f.png)
![首页-设备管理](https://user-images.githubusercontent.com/49876032/221079991-d540db54-d292-4b63-830e-0c300b10fccb.png)
![首页-设备管理2](https://user-images.githubusercontent.com/49876032/221080008-5112f2d2-e018-4379-98cb-62d93d12949d.png)
![首页-图表数据](https://user-images.githubusercontent.com/49876032/221080014-56d1ed2f-88ae-44f6-b160-04e4af30fb9f.png)
