from serial_monitor import serial_monitor
from current_time import current_time
from database import database
from camera import camera
import serial
import time
import mysql.connector
import os

count = 0
active = True
userid = 1


time.sleep(2)

current_time = current_time()
hour = current_time.get_hour()

sm = serial_monitor()

camera = camera()

db = database()
db.connect()


# Read and record the data
while active:

    distance = sm.get_distance()
    ldr = sm.get_ldr()
    
    count += 1
    time.sleep(0.1)     # wait (sleep) 0.1 seconds
    
    if count % 2 == 0 and count != 0:
        col_headers = ['sensor_values', 'distance', 'ldr', 'userid']
        col_values = [distance, ldr, userid]

        db.insert(col_headers, col_values)   

        current_hour = current_time.get_hour()

        if current_hour > hour:
            os.system("python filecontrol.py")
            hour = current_hour