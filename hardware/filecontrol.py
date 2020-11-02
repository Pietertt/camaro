import os
import time

xdays = 1
path = '/home/pi/Desktop/project/videos'
now = time.time()

files = os.listdir(path)

print("\nList all files older than " + str(xdays) + " days")
print("===========================" + "=" * len(str(xdays)) + "====")

for f in files:
	if os.stat("videos/" + f).st_mtime < now - (xdays * 86400):
		print(f)
		os.system("sudo rm videos/" + f)

print("\nList all files newer than " + str(xdays) + " days")
print("===========================" + "=" * len(str(xdays)) + "====")
for f in files:
	if os.stat("videos/" + f).st_mtime > now - (xdays * 86400):
		print(f)
