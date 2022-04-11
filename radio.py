import json
import requests
import subprocess
import time
URL = 'http://icecast.omroep.nl/3fm-sb-mp3'
PASSWORD = 'radio'
while True:
    try:
        print(subprocess.getoutput('pgrep vlc'))
        response = requests.get('http://:radio@127.0.0.1:8080/requests/status.json')
        response = json.loads(response.text)
        t0 = response['time']
        time.sleep(3)
        response = requests.get('http://:radio@127.0.0.1:8080/requests/status.json')
        response = json.loads(response.text)
        t1 = response['time']
        state = response['state']
        if t0 == t1 and state != "paused":
            requests.get('http://:radio@127.0.0.1:8080/requests/status.json?command=pl_empty')
            requests.get(f'http://:radio@127.0.0.1:8080/requests/status.json?command=in_play&input={URL}')
    except:
        subprocess.Popen(['cvlc','--intf','http','--http-password',f'{PASSWORD}'])
        time.sleep(3)
done
