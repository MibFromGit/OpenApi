import http
import requests
import rich

class Spotify_Requests:
    def __init__(self):
        self.spotify_token = 'BQAMgiqAtl12any2WZqlTCyhuEPwUV03zIrLYuo4CkMbJA3eJMawhbBZH7Gki16H0Z318TetAu_GGfRaQD372EEvnjiWD86K8_T2CPpHVkWpeG2c67cE'
        self.base_uri = 'https://api.spotify.com/v1/search/'

    def artist_albums(self, artist_id):
        self.artist_album_uri = f'https://api.spotify.com/v1/artists/{artist_id}/albums'

        response = requests.get(self.artist_album_uri)
        return response


    def get_artist_id(self, artist):
        headers = {'Authorization': f'Bearer {self.spotify_token}'}
        payload = {'type': 'artist', 'q': artist}
        r = requests.get(self.base_uri, headers=headers, params=payload)

        if (r.status_code != 200):
            print(f"Error {r.status_code}")
        return r.json()['artists']['items'][0]['id']

spotify = Spotify_Requests()

artist = input("Artist?: ")
print(spotify.artist_albums(spotify.get_artist_id(artist)))