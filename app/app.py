from curl_cffi import requests
from fastapi import FastAPI
import json
#Creating a FastAPI Instance

app=FastAPI()


headers = {
    'accept': 'application/json',
    'accept-language': 'en',
    'app-platform': 'WebPlayer',
    'authorization': 'Bearer BQBZbmfIHIyAPyBhW8AcbbO2TFmnU5Ut8Vf8Jstf28Bc1cBquDFUcTW8iBJocAidYqmBWVvDuSVvz1liVExzuKtamUk7ZyFwiSGh1fIQ4H0ww1JwMA7tvlpFHjATiBNCsrJO5bVu61o',
    'cache-control': 'no-cache',
    'client-token': 'AAB38E1NLZ5auwBrY08/YuqRtmrwsnaEXh98YUpGKnhJG7ncsT24dZMtZqNiFt/hw59cOqDLzmzFsTSq/IbDgrNGpJQ72xNvtbaKf2JHBjeSQDmhtrkeg5EUQuYrGFxwfZFwFrDK1W2tcJS9YcJod+5XrNX7d/9Tsl3qRQ6IO75xX8hhBMIj0wSXsyJ3KIapu0HouJ+xxRds4ILEjOO82eAgHnyF7EhUpJKNt/npfHGeZP4MXlPifA3gktIsvB0EiEXVHke2/3dIzup7YuefHbuTN+sDYMcCLhxpGuSpRCK8rY8HuyUD5Yh+oadJFA+r0cTnyHqnAonOBHQxZIMlUqlHsFl7YsmgwEAx',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://open.spotify.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://open.spotify.com/',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'spotify-app-version': '896000000',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
}

json_data = {
    'variables': {
        'uri': 'spotify:artist:1wRPtKGflJrBx9BmLsSwlU',
        'locale': '',
        'preReleaseV2': False,
    },
    'operationName': 'queryArtistOverview',
    'extensions': {
        'persistedQuery': {
            'version': 1,
            'sha256Hash': '7f86ff63e38c24973a2842b672abe44c910c1973978dc8a4a0cb648edef34527',
        },
    },
}

response = requests.post('https://api-partner.spotify.com/pathfinder/v2/query', headers=headers, json=json_data)
data=json.loads(response.text)
print(data)
artists_data = []
path = data.get("data", {}).get("albumUnion", {}).get("tracksV2", {}).get("items", [])

for item in path:
    track = item.get("track", {})
    artists = track.get("artists", {}).get("items", [])

    for artist in artists:
        artists_data.append({
     
        "name" : artist.get("profile", {}).get("name"),
        "uri" : artist.get("uri"),
        "artist_id" : artist.get("uri").split(":")[-1] if artist.get("uri") else None
        })
        
    
print(artists_data)
@app.get("/artists")
def get_artists():
    return artists_data