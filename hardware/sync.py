from database import database
import os

class sync:
    db = database()
    def __init__(self):
        global valid
        global userid

        valid = 1
        userid = 1


    def file_remove_local(self, directory, current_file):
	    os.system("sudo rm " + directory + "/" + current_file)

    def file_remove_database(self, current_file):
        self.db.connect()
        timestamp = os.path.splitext(current_file)[0]
        col_headers = ['activities', 'timestamp', 'valid', 'userid']
        col_values = [timestamp, valid, userid]

        self.db.delete(col_headers, col_values)
	
    def file_remove_remote(self, directory, current_file):
        os.system('ssh pieterboersma@imac-van-pieter rm /Users/pieterboersma/Desktop/camaro/frontend/public/data/' + directory + "/" + current_file)