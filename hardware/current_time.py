import datetime
import time

class current_time:
    def __init__(self):
        pass

    def get_now(self):
        return time.time()

    def get_time(self):
        return time.strftime("%Y%m%d%H%M%S")

    def get_hour(self):
        return time.strftime("%H")