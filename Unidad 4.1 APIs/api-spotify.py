import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

client_id = '6dd1cb1f607b4b53be86dc4de6c617a0'
client_secret = '89b637f4d886474db230adfb53dfba71'

clients = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

#scope = 'user-library-read'

""" 
cliente = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id, client_secret = client_secret, 
    redirect_uri='https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF',
    scope=scope
)) """

cliente = spotipy.Spotify(client_credentials_manager=clients)

playlist_link='https://open.spotify.com/artist/5eAWCfyUhZtHHtBdNk56l1?si=M6A7E1QSRsyXLoSIgTG59A'
playlist_uri = playlist_link.split('/')[-1].split("?")[0]

albumes = cliente.artist_albums(playlist_uri, album_type='album')


for album in albumes['items']:
    print(album['name'])