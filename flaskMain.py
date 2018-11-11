from flask import Flask, request, url_for
import spotipy
from spotipy import oauth2
import requests
import xmltodict
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = ''
SCOPE = 'playlist-modify-public'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )
sp = None
playlist = ''

@app.route('/police.mp3')
def police():
    try:
        return send_file('/root/dj-app/police.mp3', attachment_filename='police.mp3')
    except Exception as e:
        return str(e) 

@app.route('/')
def index():

    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token!")
        print(token_info['access_token'])
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print("Found Spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print("Access token available! Trying to get user information...")
        sp = spotipy.Spotify(access_token)

        results = sp.current_user()
        print (add_track)
        return get_playlist()

    else:
        return htmlForLoginButton()
@app.route('/process_playlist', methods=['GET'])
def process_playlist():
    global playlist
    post_data = request.args.get('playlistname','')
    print(post_data)
    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token!")
        print(token_info['access_token'])
        access_token = token_info['access_token']
    sp = spotipy.Spotify(access_token)
    result = sp.current_user()
    userID = result['id']
    playlists = sp.user_playlists(userID)
    for playlist_cur in playlists['items']:
        if playlist_cur['name'] == post_data:
            playlist = playlist_cur['id']
            print(("content of playlist variable " + playlist))
            return '<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css"><body>    <style type="text/css">        body {            background-color: #aaa;            background-image: url("https://hdwallsource.com/img/2014/9/blur-26347-27038-hd-wallpapers.jpg");            background-repeat: no-repeat;            background-position: center;            background-size: cover;            padding: 10px;        }        .form-heading {            color: #fff;            font-size: 23px;        }        .panel h2 {            color: #444444;            font-size: 18px;            margin: 0 0 8px 0;        }        .panel p {            color: #777777;            font-size: 14px;            margin-bottom: 30px;            line-height: 24px;        }        .login-form .form-control {            background: #f7f7f7 none repeat scroll 0 0;            border: 1px solid #d4d4d4;            border-radius: 4px;            font-size: 14px;            height: 50px;            line-height: 50px;        }        .main-div {            background: #ffffff none repeat scroll 0 0;            border-radius: 2px;            margin: 10px auto 30px;            max-width: 38%;            padding: 50px 70px 70px 71px;        }        .login-form .form-group {            margin-bottom: 10px;        }        .login-form {            text-align: center;        }        .forgot a {            color: #777777;            font-size: 14px;            text-decoration: underline;        }        .login-form .btn.btn-primary {            background: #f0ad4e none repeat scroll 0 0;            border-color: #f0ad4e;            color: #ffffff;            font-size: 14px;            width: 100%;            height: 50px;            line-height: 50px;            padding: 0;        }        .forgot {            text-align: left;            margin-bottom: 30px;        }        .botto-text {            color: #ffffff;            font-size: 14px;            margin: auto;        }        .login-form .btn.btn-primary.reset {            background: #ff9900 none repeat scroll 0 0;        }        .back {            text-align: left;            margin-top: 10px;        }        .back a {            color: #444444;            font-size: 13px;            text-decoration: none;        }    </style>    <div class="container">        <div class="login-form">            <div class="main-div">                <div class="panel">                    <p>Text these commands to 617-340-8468</p>                </div>                <ul class="list-group">                        <li class="list-group-item">Song Name - Artist</li>                        <li class="list-group-item">What song is playing</li>                        <li class="list-group-item">Play/Pause</li>                        <li class="list-group-item">Volume "level 0-100"</li>                        <li class="list-group-item">Shuffle</li>                </ul>            </div>        </div>    </div></body>'
            
    new_playlist = sp.user_playlist_create(userID, str(post_data))
    playlist = new_playlist['id']
    return '<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css"><body>    <style type="text/css">        body {            background-color: #aaa;            background-image: url("https://hdwallsource.com/img/2014/9/blur-26347-27038-hd-wallpapers.jpg");            background-repeat: no-repeat;            background-position: center;            background-size: cover;            padding: 10px;        }        .form-heading {            color: #fff;            font-size: 23px;        }        .panel h2 {            color: #444444;            font-size: 18px;            margin: 0 0 8px 0;        }        .panel p {            color: #777777;            font-size: 14px;            margin-bottom: 30px;            line-height: 24px;        }        .login-form .form-control {            background: #f7f7f7 none repeat scroll 0 0;            border: 1px solid #d4d4d4;            border-radius: 4px;            font-size: 14px;            height: 50px;            line-height: 50px;        }        .main-div {            background: #ffffff none repeat scroll 0 0;            border-radius: 2px;            margin: 10px auto 30px;            max-width: 38%;            padding: 50px 70px 70px 71px;        }        .login-form .form-group {            margin-bottom: 10px;        }        .login-form {            text-align: center;        }        .forgot a {            color: #777777;            font-size: 14px;            text-decoration: underline;        }        .login-form .btn.btn-primary {            background: #f0ad4e none repeat scroll 0 0;            border-color: #f0ad4e;            color: #ffffff;            font-size: 14px;            width: 100%;            height: 50px;            line-height: 50px;            padding: 0;        }        .forgot {            text-align: left;            margin-bottom: 30px;        }        .botto-text {            color: #ffffff;            font-size: 14px;            margin: auto;        }        .login-form .btn.btn-primary.reset {            background: #ff9900 none repeat scroll 0 0;        }        .back {            text-align: left;            margin-top: 10px;        }        .back a {            color: #444444;            font-size: 13px;            text-decoration: none;        }    </style>    <div class="container">        <div class="login-form">            <div class="main-div">                <div class="panel">                    <p>Text these commands to 617-340-8468</p>                </div>                <ul class="list-group">                        <li class="list-group-item">Song Name - Artist</li>                        <li class="list-group-item">What song is playing</li>                        <li class="list-group-item">Play/Pause</li>                        <li class="list-group-item">Volume "level 0-100"</li>                        <li class="list-group-item">Shuffle</li>                </ul>            </div>        </div>    </div></body>'
  


@app.route('/add_track', methods=['GET'])
def add_track():
    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token!")
        print(token_info['access_token'])
        access_token = token_info['access_token']
    sp = spotipy.Spotify(access_token)

    if sp == None:
        print('gabe this is an invalid token DAMN IT GENE')
    result = sp.current_user()

    song_name = request.args.get('song','')
    artist_name = request.args.get('artist','')
    results = sp.search(q='track:' + song_name  + ' artist:' +artist_name, type='track')

    
    items = results['tracks']['items']
    print( items)

    if len(items) > 0:
        song_id = items[0]['id']
        add_track = sp.user_playlist_add_tracks(result['id'], playlist, [song_id])
        print (add_track)
        return 'song added'
    else:
        return 'no results'

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
    print ('inside sms reply')
    if body.lower() == "what song is playing" or body.lower() == "what song is playing?":
        print('wat song playing yo')
        getURL = 'http://' + ip + ':8090/now_playing'
        ret = requests.get(getURL).content
        print(('ret '+str(ret)))
        nowPlaying = xmltodict.parse(ret.text)
        print(('nowPlaying '+str(nowPlaying)))
        now = nowPlaying.get('nowPlaying')
        print(('now '+str(now)))
        track = now.get('track')
        artist = now.get('artist')
        resp.message('The song currently playing is ' + track + ' by ' + artist)
        return str(resp)
    for i in range(101):
        if body.lower() == 'volume '+ str(i):
            postURL = 'http://'+ip+':8090/volume'
            xmlVol = '<volume>'+str(i)+'</volume>'
            send = requests.post(postURL, xmlVol)
            resp.message('The volume has been set to '+str(i)+'.')
            return str(resp)
    if body.lower() == 'pause':
        postURL = 'http://'+ip+':8090/key'
        xmlPause = "<key state='press' sender='Gabbo'>PAUSE</key>"
        send = requests.post(postURL, xmlPause)
        resp.message("The music has been paused.")
        return str(resp)
    if body.lower() == 'play':
        postURL = 'http://'+ip+':8090/key'
        xmlPlay = "<key state='press' sender='Gabbo'>PLAY</key>"
        send = requests.post(postURL, xmlPlay)
        resp.message("The music will now start playing.")
        return str(resp)
    if body.lower() == 'mute':
        postURL = 'http://'+ip+':8090/key'
        xmlMute = "<key state='press' sender='Gabbo'>MUTE</key>"
        send = requests.post(postURL, xmlMute)
        resp.message("The music is now muted.")
        return str(resp)
    if body.lower() == 'shuffle on':
        postURL = 'http://'+ip+':8090/key'
        xmlShuffleOn = "<key state='press' sender='Gabbo'>SHUFFLE_ON</key>"
        send = requests.post(postURL, xmlShuffleOn)
        resp.message("Shuffle is on.")
        return str(resp)
    if body.lower() == 'shuffle off':
        postURL = 'http://'+ip+':8090/key'
        xmlShuffleOff = "<key state='press' sender='Gabbo'>SHUFFLE_OFF</key>"
        send = requests.post(postURL, xmlShuffleOff)
        resp.message("Shuffle is off.")
        return str(resp)
    if body.lower() == 'police':
        postURL = 'http://'+ip+':8090/speaker'
        xmlPolice = "<play_info> <app_key>'dkDPjTPmDZMBHo1AADhXDIaamtL8H49S'</app_key> <url>'https://soundcloud.com/taylor-rabbitt-258669471/police-1'</url> <service>'Police Notification System'</service> </play_info>"
        send = requests.post(postURL, xmlPolice)
        resp.message("The party has been notified.")
        return str(resp)
    resp.message("Your song has been added to the queue!")
        
    return str(resp)


def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton

def getSPOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url


def get_playlist():
    enter_playlist = '<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css"><body>        <style type="text/css">            body {                background-color: #aaa;                background-image: url("https://hdwallsource.com/img/2014/9/blur-26347-27038-hd-wallpapers.jpg");                background-repeat: no-repeat;                background-position: center;                background-size: cover;                padding: 10px;            }                .form-heading {                color: #fff;                font-size: 23px;            }                .panel h2 {                color: #444444;                font-size: 18px;                margin: 0 0 8px 0;            }                .panel p {                color: #777777;                font-size: 14px;                margin-bottom: 30px;                line-height: 24px;            }                .login-form .form-control {                background: #f7f7f7 none repeat scroll 0 0;                border: 1px solid #d4d4d4;                border-radius: 4px;                font-size: 14px;                height: 50px;                line-height: 50px;            }                .main-div {                background: #ffffff none repeat scroll 0 0;                border-radius: 2px;                margin: 10px auto 30px;                max-width: 38%;                padding: 50px 70px 70px 71px;            }                .login-form .form-group {                margin-bottom: 10px;            }                .login-form {                text-align: center;            }                .forgot a {                color: #777777;                font-size: 14px;                text-decoration: underline;            }                .login-form .btn.btn-primary {                background: #f0ad4e none repeat scroll 0 0;                border-color: #f0ad4e;                color: #ffffff;                font-size: 14px;                width: 100%;                height: 50px;                line-height: 50px;                padding: 0;            }                .forgot {                text-align: left;                margin-bottom: 30px;            }                .botto-text {                color: #ffffff;                font-size: 14px;                margin: auto;            }                .login-form .btn.btn-primary.reset {                background: #ff9900 none repeat scroll 0 0;            }                .back {                text-align: left;                margin-top: 10px;            }                .back a {                color: #444444;                font-size: 13px;                text-decoration: none;            }        </style>            <div class="container">            <div class="login-form">                <div class="main-div">                    <div class="panel">                        <p>Playlist Name:</p>                    </div>                    <form action="/process_playlist">                        <div class="form-group">                            <input type="text" class="form-control" id="inputPlaylist" name="playlistname">                        </div>                <button type="submit" class="btn btn-primary">Submit</button></form></div>                                                </div>        </div>    </body>'
    return enter_playlist

