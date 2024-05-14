import requests
import json
from base64 import b64encode

def record_recognition(url, username, password, image_path):
    auth = {username:password}
    token = b64encode(json.dumps(auth).encode("utf-8"))
    my_img = {'image': open(image_path, 'rb')}
    headers = { 'Authorization' : token }
    response = requests.post(url, headers=headers, files=my_img)
    if(response.status_code != 200):
        raise Exception("Server return an error \"" + response.reason + "\" with status code " + str(response.status_code))
    
    return response
