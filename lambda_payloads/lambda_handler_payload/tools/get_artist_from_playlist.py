# Function to get the main artist from a playlist URI
import spotipy
sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

def get_artist_from_playlist(playlist_uri):
    playlist_tracks = sp.playlist_tracks(playlist_id=playlist_uri)
    artist_set = set()

    for track in playlist_tracks['items']:
        main_artist = track['track']['artists'][0]['id']
        artist_set.add(main_artist)

    return list(artist_set)