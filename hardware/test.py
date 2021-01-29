import flask
from flask import request
import os

name = 'pp'
#os.system('scp /home/pi/Desktop/project/hardware/data/images/' + name + '.png pieterboersma@imac-van-pieter:/Users/pieterboersma/Desktop/camaro/api/images')
x = os.system('curl imac-van-pieter:5000/image/validate?image=' + name + '.png')
print(x)