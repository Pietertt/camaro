from current_time import current_time
from database import database
import serial

class serial_monitor():
    ser = None
    distance = 0
    ldr = 0
    valid = 0
    def __init__(self):
        serial_monitor.ser = serial.Serial('/dev/ttyUSB0', 9600)

    def read(self, active):
        if active == True:
            serial_monitor.valid = 0
            b = serial_monitor.ser.readline()  # read a byte string
            string_n = b.decode()   # decode byte string into Unicode  
            string = string_n.rstrip() # remove \n and \r
            values = string.split('/')

            serial_monitor.distance = values[0].replace('s', '')
            serial_monitor.ldr = values[1].replace('x', '')
            serial_monitor.valid = values[2].replace('v', '')
            print(values)


    
    def get_distance(self):
        return serial_monitor.distance
    
    def get_ldr(self):
        return serial_monitor.ldr

    def get_valid(self):
        return serial_monitor.valid

 