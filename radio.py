import json, requests, subprocess, time

while True:

    if subprocess.getoutput('pgrep vlc') == "":
        subprocess.Popen(['cvlc','--intf','http','--http-password','radio','--extraintf','telnet','--telnet-password','radio'])
        time.sleep(3)

    else:
        t0 = requests.get('http://:radio@127.0.0.1:8080/requests/status.json').json()['time']
        time.sleep(3)
        t1 = requests.get('http://:radio@127.0.0.1:8080/requests/status.json').json()['time']
        state =  requests.get('http://:radio@127.0.0.1:8080/requests/status.json').json()['state']

        if t0 == t1 and state != "paused":
            requests.get('http://:radio@127.0.0.1:8080/requests/status.json?command=pl_empty')
            requests.get('http://:radio@127.0.0.1:8080/requests/status.json?command=in_play&input=http://icecast.omroep.nl/3fm-sb-mp3')

done
