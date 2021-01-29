from serial_monitor import serial_monitor
from current_time import current_time
from database import database
from pi_camera import pi_camera

db = database()
current_time = current_time()
camera = pi_camera()
sm = serial_monitor()

timestamp = (str(current_time.get_time()))
userid = str(1)

valid = camera.take_photo()
if valid == 1:
    camera.take_video(20)

db.connect()
col_headers = ['activities', 'timestamp', 'valid', 'userid']
col_values = [timestamp, str(valid), userid]

db.insert(col_headers, col_values)
