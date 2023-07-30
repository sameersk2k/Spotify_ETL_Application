# Function to recommend songs based on audio features similarity

import spotipy
import time
import random
from tools.get_artist_from_playlist import get_artist_from_playlist
from tools.calculate_similarity import calculate_similarity
sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

def recommend_similar_songs(playlist_uri, artists_limit, top_tracks_limit, recommendations_per_track, variety_factor):
    artists = get_artist_from_playlist(playlist_uri)
    recommended_songs = []
    added_track_ids = set()

    # Limit the number of artists to process
    artists = artists[:artists_limit]

    for artist_id in artists:
        top_tracks = sp.artist_top_tracks(artist_id)['tracks']

        # Limit the number of top tracks to process for each artist
        top_tracks = top_tracks[:top_tracks_limit]

        for track in top_tracks:
            audio_features = sp.audio_features(track['id'])[0]
            time.sleep(0.5)
            similar_tracks = sp.recommendations(seed_tracks=[track['id']], limit=recommendations_per_track)

            for similar_track in similar_tracks['tracks']:
                similarity_score = calculate_similarity(audio_features, sp.audio_features(similar_track['id'])[0])
                if similar_track['id'] not in added_track_ids:
                    recommended_songs.append((similar_track, similarity_score))
                    added_track_ids.add(similar_track['id'])

    recommended_songs.sort(key=lambda x: x[1], reverse=True)

    # Apply variety factor to introduce diversity in the recommendations
    variety_limit = int(recommendations_per_track * variety_factor)
    recommended_songs = recommended_songs[:recommendations_per_track]
    random.shuffle(recommended_songs)
    recommended_songs = recommended_songs[:variety_limit]

    return [track[0] for track in recommended_songs]