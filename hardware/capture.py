from current_time import current_time
from database import database
from camera import camera
import picamera

db = database()
current_time = current_time()
camera = camera()

timestamp = (str(current_time.get_time()))
valid = 1
userid = 1

camera.take_photo()
camera.take_video(20)

db.connect()
col_headers = ['activities', 'timestamp', 'valid', 'userid']
col_values = [timestamp, valid, userid]

db.insert(col_headers, col_values)



