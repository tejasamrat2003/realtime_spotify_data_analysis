import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os

# Spotify API credentials
client_id = 'your_spotify_client_id'
client_secret = 'your_spotify_client_secret'

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def fetch_playlist_tracks(playlist_id):
    """
    Fetches all track details from a Spotify playlist.
    """
    tracks = []
    results = sp.playlist_tracks(playlist_id, limit=100)
    tracks.extend(results['items'])
    
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
        
    return tracks

def save_tracks_to_csv(tracks, filename="spotify_playlist_tracks.csv"):
    """
    Saves track information to a CSV file.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Track Name', 'Artist(s)', 'Album', 'Track Duration (ms)', 'Popularity'])
        
        for item in tracks:
            track = item['track']
            track_name = track['name']
            artists = ", ".join([artist['name'] for artist in track['artists']])
            album = track['album']['name']
            duration_ms = track['duration_ms']
            popularity = track['popularity']
            
            writer.writerow([track_name, artists, album, duration_ms, popularity])

def main():
    # Replace 'your_playlist_id' with the actual Spotify playlist ID
    playlist_id = 'your_playlist_id'
    
    print(f"Fetching tracks for playlist ID: {playlist_id}")
    tracks = fetch_playlist_tracks(playlist_id)
    
    print(f"Saving {len(tracks)} tracks to CSV file.")
    save_tracks_to_csv(tracks)

if __name__ == "__main__":
    main()
