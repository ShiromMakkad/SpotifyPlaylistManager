from playlist_parser import playlist_parser
from track_list_parser import track_list_parser
from playlist_constructor import playlist_constructor
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os
import json

scope = "playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative"

if __name__ == '__main__':
    configuration = json.load(open("configuration.json"));

    os.environ['SPOTIPY_CLIENT_ID'] = configuration['client_id']
    os.environ['SPOTIPY_CLIENT_SECRET'] = configuration['client_secret']
    os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    parsed_playlists = playlist_parser(sp, configuration['playlists'])
    print("Parsed playlists!")

    track_list_parser(sp, parsed_playlists)
    print("Created track list!\n")

    playlist_constructor(sp, parsed_playlists)
    print("\nDone!")

