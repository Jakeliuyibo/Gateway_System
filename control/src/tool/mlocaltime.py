import time



def get_localtime_str_by_second():
    """ get local time """
    return time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))


def get_localtime_str_by_minute():
    """ get local time """
    return time.strftime("%Y_%m_%d_%H_%M", time.localtime(time.time()))

def get_localtime_str_by_hour():
    """ get local time """
    return time.strftime("%Y_%m_%d_%H", time.localtime(time.time()))

def get_localtime_str_by_day():
    """ get local time """
    return time.strftime("%Y_%m_%d", time.localtime(time.time()))
