import spotipy
import csv
import boto3
from datetime import datetime
import os

# Replace these imports with your actual implementation
from config.playlists import spotify_playlists
from tools.recommend_similar_songs import recommend_similar_songs

sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

# Function to write recommended songs to a CSV file
def write_to_csv(recommended_songs, csv_file):
    file_path = os.path.join('/tmp/', csv_file)  # Use the /tmp/ directory for temporary write access
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Rank', 'Track Name', 'Artist']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for rank, track in enumerate(recommended_songs, start=1):
            writer.writerow({'Rank': rank, 'Track Name': track['name'], 'Artist': track['artists'][0]['name']})
    return file_path

# Main function
def main():
    playlist_uri = spotify_playlists()['top_50_india']  # Replace with the URI of the playlist you want to use for recommendations
    artists_limit = 5  # Limit the number of artists to process
    top_tracks_limit = 10  # Limit the number of top tracks to process for each artist
    recommendations_per_track = 10  # Limit the number of recommendations generated per track
    variety_factor = 0.4  # Variety factor to introduce diversity in the recommendations

    recommended_songs = recommend_similar_songs(playlist_uri, artists_limit, top_tracks_limit, recommendations_per_track, variety_factor)

    csv_file = 'recommended_songs.csv'  # File name for the CSV output
    filepath = write_to_csv(recommended_songs, csv_file)

    # Upload the file to S3 bucket
    s3_resource = boto3.resource('s3')
    date = datetime.now()
    filename = f'spotify_playlist_{date.year}_{date.month}_{date.day}.csv'
    response = s3_resource.Object('spotify-d', filename).upload_file(filepath)

    return response

def lambda_handler(event, context):
    main()

# For local testing, you can uncomment the lines below:
# if __name__ == "__main__":
#     main()
