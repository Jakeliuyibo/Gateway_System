import os, sys, time
from driver.mserial    import *


class mSatelliteDevice(object):
    """_summary_
    achieve satellite communication device, wihch is a serial device and based on AT command
    Args:
        port             : port name
        timeout          : port configure and IO out-time , if time=0 : no wait, else wait (time) seconds
    """
    def __init__(self, port, timeout=5):
        """ init satellite device   """
        self._port = port

        # init flag
        self._flagOpen           = False

    def isOpen(self):
        """ detect satellite is open            """
        return self._flagOpen

    def isReadable(self):
        """ detect satellite is readable        """
        return self._serial.isReadable()

    def open(self):
        """ open satellite device               """
        try:
            self._serial = mSerial(self._port, baud_rate=115200, timeout=5)
            self._flagOpen       = True
            self.write("init ok")
        except Exception as e:
            self._serial = None
            self._flagOpen       = False
            print("ERROR   : Open Satellite", self._port)

    def close(self):
        """ open satellite device               """
        try:
            self._serial.close()
            self._flagOpen       = False
        except Exception as e:
            print("ERROR   : Close Satellite", self._port)

    def write(self, data):
        """ write data to satellite device      """
        try:
            if self._serial.isOpen():
                # write data to serial
                self._serial.write(data)
            else:
                raise
        except Exception as e:
            print("ERROR   : Write Satellite", self._port)

    def read(self):
        """ read data from satellite device     """
        try:
            if self.isOpen():
                # open storage file
                if self.isReadable():
                    return self._serial.read()
                else:
                    return None
            else:
                raise
        except Exception as e:
            print("ERROR   : Read Device", self._device)

    def communicate(self, cmd):
        """ send AT command and wait a reply    """
        try:
            self._serial.write(cmd+"\r\n")
            reply = self._serial.readuntil(b'\n')
            if reply:
                return reply.replace("\r\n", "")
            else:
                raise IOError
        except Exception as e:
            print("ERROR   : Communicate Satellite", self._port)

    def match(self):
        """ match device            """
        if self._serial.isOpen():
            if "ok" == self.communicate("AT"):
                return True
            else:
                return False


def test_for_connect_satellite_device(device='/dev/ttyUSB0'):
    try:
        msatellite = mSatelliteDevice(device, timeout=5)
        msatellite.open()
        if not msatellite.isOpen():
            raise
        else:
            try:
                if msatellite.match():
                    print("SUCCESS : Connect Serial %s"%msatellite._port)
                    msg = msatellite.communicate("AT+Cmd=1")
                    if msg:
                        print("SUCCESS : Communicate Serial %s %s"%(msatellite._port, msg))
                    else:
                        raise
                else:
                    raise
            except Exception as e:
                print("exception ",e)
            finally:
                msatellite.close()
    except Exception as e:
        print("test_for_connect_satellite_device error ",e)


if __name__ == "__main__":
    test_for_connect_satellite_device()