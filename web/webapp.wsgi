import os
import sys

# # Linux version
# BASE_DIR = os.path.abspath( os.path.dirname( os.path.dirname(__file__) ) )
# sys.path.append(BASE_DIR)
# sys.path.insert(0, r"/home/nano/Gateway_System/web")
# sys.path.insert(0, r"/home/nano/Gateway_System/web/app")
# sys.path.insert(0, r"/usr/lib/python3.8")
# sys.path.insert(0, r"/home/nano/.local/lib/python3.8/site-packages")

# Windows version
sys.path.insert(0, r"Y:\Studyplace_Web_Development\Gateway_System\web")
sys.path.insert(0, r"Y:\Studyplace_Web_Development\Gateway_System\web\app")
from app import create_app

application = create_app("develop")

# def application(environ,start_response):
#     status = "200 Ok"
#     output = b"Hello wsgi"
#     response_headers=[('Content-type','text/plain'),('Content-Length',str(len(output)))]
#     start_response(status,response_headers)
#     return[output]