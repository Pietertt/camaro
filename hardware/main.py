from serial_monitor import serial_monitor
from current_time import current_time
from filecontrol import filecontrol
from database import database
import serial
import time
import mysql.connector
import os

count = 0
userid = str(1)
active = True

time.sleep(2)

current_time = current_time()
hour = current_time.get_hour()

sm = serial_monitor()

filecontrol = filecontrol()

db = database()
db.connect()

# Read and record the data
while active:
    sm.read(True)
    distance = str(sm.get_distance())
    ldr = str(sm.get_ldr())
    valid = int(sm.get_valid())

    if int(distance) != 0 and int(distance) < 20 and valid == 1:
        sm.read(False)
        print("CAPTURE")
        os.system('python capture.py')
        sm.read(True)
    
    count += 1
    time.sleep(0.1)     # wait (sleep) 0.1 seconds
    
    if count % 2 == 0 and count != 0:
        col_headers = ['sensor_values', 'distance', 'ldr', 'userid']
        col_values = [distance, ldr, userid]

        db.insert(col_headers, col_values)

        current_hour = current_time.get_hour()

        if current_hour > hour: #previous current_hour > hour
            filecontrol.file_check()
            hour = current_hour