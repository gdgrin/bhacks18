import requests
import xmltodict
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])


def sms_reply():
    body = request.values.get('Body', None)
    song_info = body.lower()
    if '-' in song_info: 
        song_info = song_info.split('-')
        song = song_info[0]
        artist = song_info[1]
    ip = "172.20.10.5"    

    resp = MessagingResponse()
 
    if body.lower() == "what song is playing" or body.lower() == "what song is playing?":
        getURL = f'http://{ip}:8090/now_playing'
        ret = requests.get(getURL)
        nowPlaying = xmltodict.parse(ret.text)
        now = nowPlaying.get('nowPlaying')
        track = now.get('track')
        artist = now.get('artist')
        resp.message(f'The song currently playing is {track} by {artist}.')
        return str(resp)
    for i in range(101):
        if body.lower() == f'volume {i}':
            postURL = f'http://{ip}:8090/volume'
            xmlVol = f'<volume>{i}</volume>'
            send = requests.post(postURL, xmlVol)
            resp.message(f'The volume has been set to {i}.')
            return str(resp)
    if body.lower() == 'pause':
        postURL = f'http://{ip}:8090/key'
        xmlPause = "<key state='press' sender='Gabbo'>PAUSE</key>"
        send = requests.post(postURL, xmlPause)
        resp.message("The music has been paused.")
        return str(resp)
    if body.lower() == 'play':
        postURL = f'http://{ip}:8090/key'
        xmlPlay = "<key state='press' sender='Gabbo'>PLAY</key>"
        send = requests.post(postURL, xmlPlay)
        resp.message("The music will now start playing.")
        return str(resp)
    if body.lower() == 'mute':
        postURL = f'http://{ip}:8090/key'
        xmlMute = "<key state='press' sender='Gabbo'>MUTE</key>"
        send = requests.post(postURL, xmlMute)
        resp.message("The music is now muted.")
        return str(resp)
    if body.lower() == 'shuffle on':
        postURL = f'http://{ip}:8090/key'
        xmlShuffleOn = "<key state='press' sender='Gabbo'>SHUFFLE_ON</key>"
        send = requests.post(postURL, xmlShuffleOn)
        resp.message("Shuffle is on.")
        return str(resp)
    if body.lower() == 'shuffle off':
        postURL = f'http://{ip}:8090/key'
        xmlShuffleOff = "<key state='press' sender='Gabbo'>SHUFFLE_OFF</key>"
        send = requests.post(postURL, xmlShuffleOff)
        resp.message("Shuffle is off.")
        return str(resp)
    if body.lower() == 'police':
        postURL = f'http://{ip}:8090/speaker'
        xmlPolice = "<play_info> <app_key>'dkDPjTPmDZMBHo1AADhXDIaamtL8H49S'</app_key> <url>'https://soundcloud.com/taylor-rabbitt-258669471/police-1'</url> <service>'Police Notification System'</service> </play_info>"
        send = requests.post(postURL, xmlPolice)
        resp.message("The party has been notified.")
        return str(resp)
    resp.message("Your song has been added to the queue!")
        
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
