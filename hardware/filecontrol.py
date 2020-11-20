from serial_monitor import serial_monitor
from current_time import current_time
from database import database
import os

xdays = 1
valid = 1
userid = 1
path = '/home/pi/Desktop/project/hardware/videos'

current_time = current_time()
db = database()
files = os.listdir(path)

print("\nList all files older than " + str(xdays) + " days")
print("===========================" + "=" * len(str(xdays)) + "====")

for current_file in files:
	if os.stat("videos/" + current_file).st_mtime < current_time - (xdays * 86400):
		print(current_file)
		db.connect()
		col_headers = ['activities', 'timestamp', 'valid', 'userid']
		col_values = [current_file, valid, userid]

		db.delete(col_headers, col_values) 

print("\nList all files newer than " + str(xdays) + " days")
print("===========================" + "=" * len(str(xdays)) + "====")
for current_file in files:
	if os.stat("videos/" + current_file).st_mtime > current_time - (xdays * 86400):
		print(current_file)
