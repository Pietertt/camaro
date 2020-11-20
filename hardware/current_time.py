import datetime
import time

class current_time:
    def __init__(self):
        global time
        time = datetime.datetime.now()

    def get_time(self):
        return time.strftime("%Y%m%d%H%M%S")

    def get_hour(self):
        return time.strftime("%H")