import pprint

import requests


def get_album(album_id):
    album = requests.get(f"https://jsonplaceholder.typicode.com/albums/{album_id}").json()
    album["user"] = requests.get(f"https://jsonplaceholder.typicode.com/users/{album['userId']}").json()
    album["photos"] = requests.get(f"https://jsonplaceholder.typicode.com/photos?albumId={album['id']}").json()
    return album


pprint.pprint(get_album(42))
