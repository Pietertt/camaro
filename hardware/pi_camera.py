
from current_time import current_time
from filecontrol import filecontrol
import requests
import subprocess
import picamera
import time
import json
import os

class pi_camera:
  name = '0'
  def __init__(self):
    global camera 
    global filecontrol
    global valid

    camera = picamera.PiCamera()
    filecontrol = filecontrol()

    camera.framerate = 25
    camera.resolution = (128, 128)
    camera.vflip = True
    camera.hflip = True

  def take_photo(self):
    valid = 0
    pi_camera.name = str(current_time().get_time())
    camera.capture(pi_camera.name + ".jpg")
    os.system("sudo mv " + pi_camera.name + ".jpg data/images")
    time.sleep(1)
    
    os.system('scp /home/pi/Desktop/project/hardware/data/images/' + pi_camera.name + '.jpg pieterboersma@imac-van-pieter:/Users/pieterboersma/Desktop/camaro/api/images')
    time.sleep(2)
    #valid = json.loads(requests.get('http://imac-van-pieter:5000/image/validate?image=' + pi_camera.name + '.jpg').text)
    valid = json.loads(requests.get('http://imac-van-pieter:5000/image/validate?image=' + "testimage" + '.jpg').text)
    print('Value of valid is: ')
    print(valid)

    if valid > 0.5:
      os.system('scp /home/pi/Desktop/project/hardware/data/images/' + pi_camera.name + '.jpg pieterboersma@imac-van-pieter:/Users/pieterboersma/Desktop/camaro/frontend/public/data/images')
      time.sleep(1)
    elif valid < 0.5:
      os.system("sudo rm data/images/" + pi_camera.name + ".jpg")

    os.system('ssh pieterboersma@imac-van-pieter rm /Users/pieterboersma/Desktop/camaro/api/images/' + pi_camera.name + '.jpg')
      
    return valid

  def take_video(self, recording_time):
    camera.resolution = (1920, 1080)
    self.recording_time = recording_time
    
    camera.start_preview()
    time.sleep(1)
    camera.start_recording(pi_camera.name + ".h264")
    time.sleep(recording_time)
    camera.stop_recording()
    camera.stop_preview()
    os.system("MP4Box -add " + pi_camera.name + '.h264 ' + pi_camera.name + '.mp4')
    time.sleep(2)
    os.system("sudo mv " + pi_camera.name + ".mp4 data/videos")
    time.sleep(1)
    os.system('scp /home/pi/Desktop/project/hardware/data/videos/' + pi_camera.name + '.mp4 pieterboersma@imac-van-pieter:/Users/pieterboersma/Desktop/camaro/frontend/public/data/videos')
    os.system('sudo rm ' + pi_camera.name + '.h264')
    time.sleep(3)
