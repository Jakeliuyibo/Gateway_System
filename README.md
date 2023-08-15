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

![登录界面](https://github.com/Jakeliuyibo/Gateway_System/assets/49876032/9baa0132-58d1-4a10-b7ab-10a45f8d69aa)
![设备信息页面](https://github.com/Jakeliuyibo/Gateway_System/assets/49876032/b0d702c1-7c6c-422d-b5df-875c35716600)
![本地文件页面](https://github.com/Jakeliuyibo/Gateway_System/assets/49876032/6a94dfd0-cd81-4623-97c0-c5ac0464961a)
![任务管理页面](https://github.com/Jakeliuyibo/Gateway_System/assets/49876032/9b80cfef-2f1f-4ced-9a52-50d0dde1d371)
![设备流量页面](https://github.com/Jakeliuyibo/Gateway_System/assets/49876032/cb58c34a-624e-4081-a2b9-5ffdc09be168)
