from current_time import current_time
import picamera
import time
import os

class pi_camera:
  name = '0'
  def __init__(self):
    global camera 

    camera = picamera.PiCamera()
    camera.framerate = 25
    camera.resolution = (640, 480)
    camera.vflip = True
    camera.hflip = True
  
  def take_video(self, recording_time):

    self.recording_time = recording_time
    pi_camera.name = str(current_time().get_time())
    
    camera.start_preview()
    time.sleep(1)
    camera.start_recording(pi_camera.name + ".h264")
    time.sleep(recording_time)
    camera.stop_recording()
    camera.stop_preview()
    os.system("sudo mv " + pi_camera.name + ".h264 videos")
    time.sleep(3)

  def take_photo(self):
    camera.capture(pi_camera.name + ".jpg")   
    os.system("sudo mv " + pi_camera.name + ".jpg images")
    time.sleep(1)

