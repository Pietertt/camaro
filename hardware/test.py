import requests
import json

print(json.loads(requests.get('http://imac-van-pieter:5000/image/validate?image=testimage.jpg').text))

#print(subprocess.check_output(["curl http://google.com/"]))
