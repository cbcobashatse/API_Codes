import requests
import spotipy

CLIENT_ID = '92e33f2cb60a4788be53e6f0352b00ac'
CLIENT_SECRET = 'c0598a796ad64991abae0be8b0fa1d55'
AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
  'grant_type' : 'client_credentials',
  'client_id' : CLIENT_ID,
  'client_secret' : CLIENT_SECRET,
})

#convert the response to JSON
auth_response_data = auth_response.json()

print(auth_response.status_code)
print(auth_response_data)