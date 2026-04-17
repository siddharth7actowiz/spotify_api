import requests
from fastapi import FastAPI
import json
#Creating a FastAPI Instance

app=FastAPI()



headers = {
    'accept': 'application/json',
    'accept-language': 'en',
    'app-platform': 'WebPlayer',
    'authorization': 'Bearer BQDdFDGWbIXIp0CCPdIk8vKfDioD9gpM_8fzkeZ47VHsHCR5UxHJEAL5eaTMoS4WQ716x9JTRoj7CBgo0acI2B_-F4oL4I8J2Lk-8zQ9ZywBIwA0K7OIO-ZI13fBJlKy0Lv2ULAZjmw',
    'cache-control': 'no-cache',
    'client-token': 'AAB9rgGNn2APLxRiaxH+Pt3VXoJpC/s5FkLSJNDajou2QLN+8az8Q/gOYcze5fttek4bnJ0/txJFABUPJj0tEkerddCum+K7EzBmgRcApC/RPnRtALoGH2xk+BJ7DKWqSQZGgWwnFyGqobGPGH8KxkiY17Fqi3o5/tPjJLY4Glr8nggs9bfm7OUGlOG8NwPOpxPLbAWQSqyk8lr/EZ0QrguFPmLER1CICpJEZHzYWp6Qti+EA9p4XN7qs3M+IIiQAI2mV1/V2Iwn5Da0nBZuayAdRM8SRZ3XNs9MAZa6Paqv455jWg1iooDJGNn8NXORyncOPworMwdJqTcMQi0avaanmXmMfEP08/Q=',
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
    'spotify-app-version': '1.2.89.2.g66a2067b',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
}

json_data = {
    'variables': {
        'uri': 'spotify:section:0JQ5DAnM3wGh0gz1MXnu3C',
        'homeEndUserIntegration': 'INTEGRATION_WEB_PLAYER',
        'timeZone': 'Asia/Calcutta',
        'sp_t': 'd704ac76-c178-4b8c-921c-df91228c7fd7',
        'sectionItemsOffset': 0,
        'sectionItemsLimit': 20,
    },
    'operationName': 'homeSection',
    'extensions': {
        'persistedQuery': {
            'version': 1,
            'sha256Hash': '23e37f2e58d82d567f27080101d36609009d8c3676457b1086cb0acc55b72a5d',
        },
    },
}

response = requests.post('https://api-partner.spotify.com/pathfinder/v2/query', headers=headers, json=json_data)
data=json.loads(response.text)
artists_data = []

sections = data.get("data", {}).get("homeSections", {}).get("sections", [])

for section in sections:
    items = section.get("sectionItems", {}).get("items", [])
    
    for item in items:
        artist = item.get("content", {}).get("data", {})
        profile = artist.get("profile", {})
        visuals = artist.get("visuals", {})
        
        # Get image URL (largest = 640px)
        sources = visuals.get("avatarImage", {}).get("sources", [])
        image_url = sources[0].get("url") if sources else None
        
        artists_data.append({
            "name": profile.get("name"),
             "url": f"https://open.spotify.com/artist/{artist.get('uri', '').split(':')[-1]}",
            "artist_id": artist.get("uri", "").split(":")[-1],
            "image_url": image_url
        })

@app.get("/artists")
def get_artists():
    return artists_data