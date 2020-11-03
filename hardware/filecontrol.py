import os
import time
import mysql.connector

xdays = 1
path = '/home/pi/Desktop/project/hardware/videos'
now = time.time()

files = os.listdir(path)

print("\nList all files older than " + str(xdays) + " days")
print("===========================" + "=" * len(str(xdays)) + "====")

for f in files:
	if os.stat("videos/" + f).st_mtime < now - (xdays * 86400):
		print(f)
		database = mysql.connector.connect(
			host="imac-van-pieter",
			user="root",
			password="root",
			database="camaro",
			port="3306"
		)
		mycursor = database.cursor()

		sql = "DELETE FROM `activities` (`ID`, `timestamp`, `valid`, `userid`) VALUES (NULL, %s, %s, %s)"
		val = (f, '1', '1')
		mycursor.execute(sql, val)

		database.commit()

		print(mycursor.rowcount, "record removed.")		
		os.system("sudo rm videos/" + f)

print("\nList all files newer than " + str(xdays) + " days")
print("===========================" + "=" * len(str(xdays)) + "====")
for f in files:
	if os.stat("videos/" + f).st_mtime > now - (xdays * 86400):
		print(f)
