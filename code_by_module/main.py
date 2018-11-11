from bottle import route, run, request
import spotipy
from spotipy import oauth2

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = 'd6c6e5ce225342978a3e5c8b81dfdc73'
SPOTIPY_CLIENT_SECRET = 'd1239756496843f490e54230cc088a5e'
SPOTIPY_REDIRECT_URI = 'http://206.81.8.75:8080/'
SCOPE = 'playlist-modify-public'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )
sp = None
playlist = ''
@route('/')
def index():

    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print "Found cached token!"
        print token_info['access_token']
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print "Found Spotify auth code in Request URL! Trying to get valid access token..."
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print "Access token available! Trying to get user information..."
        sp = spotipy.Spotify(access_token)

        results = sp.current_user()
        print (add_track)
        return get_playlist()

    else:
        return htmlForLoginButton()
@route('/process_playlist', methods=['GET'])
def process_playlist():
    global playlist
    post_data = request.query['playlistname']
    print(post_data)
    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print "Found cached token!"
        print token_info['access_token']
        access_token = token_info['access_token']
    sp = spotipy.Spotify(access_token)
    result = sp.current_user()

    playlists = sp.user_playlists(result['id'])
    for playlist_cur in playlists['items']:
        if playlist_cur['name'] == post_data:
            playlist = playlist_cur['id']
            print("content of playlist variable " + playlist)
            return "COOL NOW TEXT: 617-340-8468 to add songs to the playlist"

      


@route('/add_track', methods=['GET'])
def add_track():
    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print "Found cached token!"
        print token_info['access_token']
        access_token = token_info['access_token']
    sp = spotipy.Spotify(access_token)

    if sp == None:
        print('gabe this is an invalid token DAMN IT GENE')
    result = sp.current_user()

    song_name = request.query['song']
    artist_name = request.query['artist']
    results = sp.search(q='track:' + song_name  + ' artist:' +artist_name, type='track')

    
    items = results['tracks']['items']
    print( items)

    if len(items) > 0:
        song_id = items[0]['id']
        add_track = sp.user_playlist_add_tracks(result['id'], playlist, [song_id])
        print (add_track)
    else:
        return 'no results'




def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton

def getSPOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url


def get_playlist():
    enter_playlist = "<form action='/process_playlist'> Enter Playlist Name :<br>  <input type='text' name='playlistname'><br> <input type='submit' value='Submit'>"
    return enter_playlist


run(host='206.81.8.75', port=8080)