from current_time import current_time
from database import database
from camera import camera
import serial

class serial_monitor():
    def __init__(self):
        global ser
        global camera
        global distance
        global ldr

        ser = serial.Serial('/dev/ttyUSB0', 9600)
        self.camera = camera()
        distance = None
        ldr = None
        
    def read(self):
        b = ser.readline()  # read a byte string
        string_n = b.decode()   # decode byte string into Unicode  
        string = string_n.rstrip() # remove \n and \r

        if 's' in string:
            distance = string.replace('s', '')
            if int(distance) < 20:
                print("CAPTURE")
                self.camera.take_video(20)
        else:
            ldr = string.replace('x', '')
    
    def get_distance(self):
        return distance
    
    def get_ldr(self):
        return ldr

 