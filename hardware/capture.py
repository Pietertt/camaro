import picamera
import time
import os
import datetime
import mysql.connector

current_time = datetime.datetime.now()

name = str(current_time.strftime("%Y%m%d%H%M%S%f")) + '.h264'

camera = picamera.PiCamera()
camera.framerate = 25
camera.resolution = (640, 480)
camera.vflip = True
camera.hflip = True

camera.start_preview()
time.sleep(1)

camera.start_recording(name)
time.sleep(20)
camera.stop_recording()
camera.stop_preview()

time.sleep(2)

os.system("sudo mv " + name + " /home/pi/Desktop/project/videos")

database = mysql.connector.connect(
  host="imac-van-pieter",
  user="root",
  password="root",
  database="camaro",
  port="3306"
)

mycursor = database.cursor()

sql = "INSERT INTO `activities` (`ID`, `timestamp`, `valid`) VALUES (NULL, %s, %s)"
val = (name, '1')
mycursor.execute(sql, val)

database.commit()

print(mycursor.rowcount, "record inserted.")