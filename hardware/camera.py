from current_time import current_time
import picamera
import time
import os

class camera:
  def __init__(self):
    global camera 

    camera = picamera.PiCamera()
    camera.framerate = 25
    camera.resolution = (640, 480)
    camera.vflip = True
    camera.hflip = True
  
  def take_video(self, recording_time):
    global name

    self.recording_time = recording_time
    name = str(current_time().get_time())
    
    camera.start_preview()
    time.sleep(1)
    camera.start_recording(name + ".h264")
    time.sleep(recording_time)
    camera.stop_recording()
    camera.stop_preview()
    os.system("sudo mv " + name + ".h264 videos")

  def take_photo(self):
    camera.capture(name + ".jpg")   
    os.system("sudo mv " + name + ".jpg images")

