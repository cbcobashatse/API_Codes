import requests
import spotipy

CLIENT_ID = '92e33f2cb60a4788be53e6f0352b00ac'
CLIENT_SECRET = 'c0598a796ad64991abae0be8b0fa1d55'
AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response_post = requests.post(AUTH_URL, {
  'grant_type' : 'client_credentials',
  'client_id' : CLIENT_ID,
  'client_secret' : CLIENT_SECRET,
})

auth_response_post_data = auth_response_post.json()

access_token = auth_response_post_data['access_token']
headers = {
        'Authorization' : 'Bearer {token}'.format(token=access_token)
        }

BASE_URL = 'https://api.spotify.com/v1/'

artist_id = '36QJpDe2go2KgaRleHCDTp'

auth_response_get = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', headers=headers, params={'include_groups' : 'album', 'limit': 1})

#convert the response to JSON
auth_response_get_data = auth_response_get.json()

print(auth_response_get.status_code)
print(auth_response_get_data)
