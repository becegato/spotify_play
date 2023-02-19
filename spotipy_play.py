import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configurar as credenciais de autenticação
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='CLIENT_ID',
                                               client_secret='CLIENT_SECRET',
                                               redirect_uri='REDIRECT_URI',
                                               scope='user-modify-playback-state'))

# Escolha a playlist que você deseja tocar
playlist_uri = 'spotify:playlist:PLAYLIST_ID'

# Obter o URI da playlist
playlist = sp.playlist(playlist_uri)
tracks = playlist['tracks']
uri_list = [track['track']['uri'] for track in tracks['items']]

# Começar a tocar a playlist
sp.start_playback(uris=uri_list)
