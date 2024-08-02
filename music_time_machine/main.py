from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "92a887b89cba445aac1153f6cd2af7b4"
CLIENT_SECRET = "633a2dfb55be49a1a70b0f1d1f983271"

date_input = input("Which do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{date_input}"
response = requests.get(URL)
webpage =response.text
class_name = "a-no-trucate"
soup = BeautifulSoup(webpage, "html.parser")
hot_100 = soup.find_all(name="h3", class_=class_name) 
# song_name = hot_100.getText().strip()
# print(song_name)
song_names = []
for name in hot_100:
    to_add = name.getText().strip()
    song_names.append(to_add)
    
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="315zbtzfme2ipieknee4wmwdv4na", 
    )
)
user_id = sp.current_user()["id"]

song_uris = []

year = date_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
        
new_playlist_name = f"{date_input} Billboard 100"

playlist = sp.user_playlist_create(user_id, new_playlist_name, public = False, collaborative = False, description = "makes a playlist of billboard's top 100 songs for that date.")
playlist_id = playlist["id"]

sp.user_playlist_add_tracks(user_id, playlist_id, song_uris, position=None)