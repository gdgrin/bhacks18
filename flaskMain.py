from flask import Flask, request, url_for,jsonify
import spotipy
from spotipy import oauth2
import requests
import xmltodict
from twilio.twiml.messaging_response import MessagingResponse
'''Global variables to keep track of DJ account and playlist ID'''
app = Flask(__name__)


SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = ''
SCOPE = 'playlist-modify-public'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )
sp = None
playlist = ''
playlist_url = ''


'''index page. if the DJ has connected Decentralized DJ before access the token 
   from cache. otherwise prompt them to connect to spotify'''
@app.route('/')
def index():

    access_token = ""

    token_info = sp_oauth.get_cached_token()
    '''oauth info'''
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
'''process  the playlist the DJ wants users to add songs to'''
@app.route('/process_playlist', methods=['GET'])
def process_playlist():
    '''get access token for spotify'''
    global playlist
    global playlist_url
    post_data = request.args.get('playlistname','')
    print(post_data)
    access_token = ""

    token_info = sp_oauth.get_cached_token()
    '''more oauth'''
    if token_info:
        print("Found cached token!")
        print(token_info['access_token'])
        access_token = token_info['access_token']
    sp = spotipy.Spotify(access_token)
    result = sp.current_user()
    userID = result['id']
    #get playlist ID if it exists else create the playlist for the DJ
    playlists = sp.user_playlists(userID)
    for playlist_cur in playlists['items']:
        if playlist_cur['name'] == post_data:
            playlist = playlist_cur['id']
            print(("content of playlist variable " + playlist))
            playlist_url = playlist_cur['external_urls']['spotify']
            print(str(playlist_url))
            return '<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css"><body>    <style type="text/css">        body {            background-color: #aaa;            background-image: url("https://hdwallsource.com/img/2014/9/blur-26347-27038-hd-wallpapers.jpg");            background-repeat: no-repeat;            background-position: center;            background-size: cover;            padding: 10px;        }        .form-heading {            color: #fff;            font-size: 23px;        }        .panel h2 {            color: #444444;            font-size: 18px;            margin: 0 0 8px 0;        }        .panel p {            color: #777777;            font-size: 14px;            margin-bottom: 30px;            line-height: 24px;        }        .login-form .form-control {            background: #f7f7f7 none repeat scroll 0 0;            border: 1px solid #d4d4d4;            border-radius: 4px;            font-size: 14px;            height: 50px;            line-height: 50px;        }        .main-div {            background: #ffffff none repeat scroll 0 0;            border-radius: 2px;            margin: 10px auto 30px;            max-width: 38%;            padding: 50px 70px 70px 71px;        }        .login-form .form-group {            margin-bottom: 10px;        }        .login-form {            text-align: center;        }        .forgot a {            color: #777777;            font-size: 14px;            text-decoration: underline;        }        .login-form .btn.btn-primary {            background: #f0ad4e none repeat scroll 0 0;            border-color: #f0ad4e;            color: #ffffff;            font-size: 14px;            width: 100%;            height: 50px;            line-height: 50px;            padding: 0;        }        .forgot {            text-align: left;            margin-bottom: 30px;        }        .botto-text {            color: #ffffff;            font-size: 14px;            margin: auto;        }        .login-form .btn.btn-primary.reset {            background: #ff9900 none repeat scroll 0 0;        }        .back {            text-align: left;            margin-top: 10px;        }        .back a {            color: #444444;            font-size: 13px;            text-decoration: none;        }    </style>    <div class="container">        <div class="login-form">            <div class="main-div">                <div class="panel">                    <p>Text these commands to 617-340-8468</p>                </div>                <ul class="list-group">                        <li class="list-group-item">Song Name-Artist</li>                        <li class="list-group-item">What song is playing?</li>                        <li class="list-group-item">Play/Pause</li> <li class="list-group-item">Mute</li>                         <li class="list-group-item">Volume "level 0-100"</li>          <li class="list-group-item">What playlist is playing?</li>              <li class="list-group-item">Shuffle On/Off</li>                </ul>            </div>        </div>    </div></body>'
            
    new_playlist = sp.user_playlist_create(userID, str(post_data))
    playlist_url = new_playlist['external_urls']['spotify']
    playlist = new_playlist['id']
    return '<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css"><body>    <style type="text/css">        body {            background-color: #aaa;            background-image: url("https://hdwallsource.com/img/2014/9/blur-26347-27038-hd-wallpapers.jpg");            background-repeat: no-repeat;            background-position: center;            background-size: cover;            padding: 10px;        }        .form-heading {            color: #fff;            font-size: 23px;        }        .panel h2 {            color: #444444;            font-size: 18px;            margin: 0 0 8px 0;        }        .panel p {            color: #777777;            font-size: 14px;            margin-bottom: 30px;            line-height: 24px;        }        .login-form .form-control {            background: #f7f7f7 none repeat scroll 0 0;            border: 1px solid #d4d4d4;            border-radius: 4px;            font-size: 14px;            height: 50px;            line-height: 50px;        }        .main-div {            background: #ffffff none repeat scroll 0 0;            border-radius: 2px;            margin: 10px auto 30px;            max-width: 38%;            padding: 50px 70px 70px 71px;        }        .login-form .form-group {            margin-bottom: 10px;        }        .login-form {            text-align: center;        }        .forgot a {            color: #777777;            font-size: 14px;            text-decoration: underline;        }        .login-form .btn.btn-primary {            background: #f0ad4e none repeat scroll 0 0;            border-color: #f0ad4e;            color: #ffffff;            font-size: 14px;            width: 100%;            height: 50px;            line-height: 50px;            padding: 0;        }        .forgot {            text-align: left;            margin-bottom: 30px;        }        .botto-text {            color: #ffffff;            font-size: 14px;            margin: auto;        }        .login-form .btn.btn-primary.reset {            background: #ff9900 none repeat scroll 0 0;        }        .back {            text-align: left;            margin-top: 10px;        }        .back a {            color: #444444;            font-size: 13px;            text-decoration: none;        }    </style>    <div class="container">        <div class="login-form">            <div class="main-div">                <div class="panel">                    <p>Text these commands to 617-340-8468</p>                </div>                <ul class="list-group">                        <li class="list-group-item">Song Name-Artist</li>                        <li class="list-group-item">What song is playing?</li>                        <li class="list-group-item">Play/Pause</li> <li class="list-group-item">Mute</li>                        <li class="list-group-item">Volume "level 0-100"</li>                 <li class="list-group-item">What playlist is playing?</li>        <li class="list-group-item">Shuffle On/Off</li>                </ul>            </div>        </div>    </div></body>'
  

#service that twilio SMS hits to add songs to queue
@app.route('/add_track', methods=['GET'])
def add_track():
    #get access token
    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token!")
        print(token_info['access_token'])
        access_token = token_info['access_token']
    sp = spotipy.Spotify(access_token)

    if sp == None:
        print('gabe this is an invalid token $#$#! GENE')
    result = sp.current_user()
    #get song and artist from get variables
    song_name = request.args.get('song','')
    artist_name = request.args.get('artist','')
    #spotify api call 
    results = sp.search(q='track:' + song_name  + ' artist:' +artist_name, type='track')
    

    items = results['tracks']['items']
    print( items)
    #add the first song that comes 
    if len(items) > 0:
        song_id = items[0]['id']
        add_track = sp.user_playlist_add_tracks(result['id'], playlist, [song_id])
        print (add_track)
        return 'song added'
    else:
        return 'no results'
#service to return playlist url
@app.route('/geturl', methods=['GET'])
def geturl():
    global playlist_url
   
    return jsonify(url=playlist_url) 


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


