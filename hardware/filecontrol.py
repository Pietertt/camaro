from current_time import current_time
from sync import sync
import time
import os

class filecontrol:
	current_time = current_time()
	sync = sync()

	def __init__(self):
		global xdays
		global userid
		global path
		global directories

		xdays = 1
		userid = 1
		path = '/home/pi/Desktop/project/hardware/data'

		directories = os.listdir(path)


	def file_check(self):

		print("\nList all files older than " + str(xdays) + " days")
		print("===========================" + "=" * len(str(xdays)) + "====")

		for directory in directories:
			files = os.listdir((path + "/" + directory))
			for current_file in files:
			# for current_file in path:
			# 	print(current_file)	
				if (os.stat(path + "/" + directory + "/" + current_file).st_mtime) < (self.current_time.get_now() - xdays * 86400):
					print(current_file)
					self.sync.file_remove_local(directory, current_file)
					self.sync.file_remove_database(current_file)
					self.sync.file_remove_remote(directory, current_file)



			print("\nList all files newer than " + str(xdays) + " days")
			print("===========================" + "=" * len(str(xdays)) + "====")
			for current_file in files:
				if (os.stat(path + "/" + directory + "/" + current_file).st_mtime) > (self.current_time.get_now() - xdays * 86400):
					print(current_file)
		



