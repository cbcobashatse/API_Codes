import requests
import pyyoutube

from youtube_api import YouTubeDataAPI

api_key = 'AIzaSyC8ScUbhEYWOFOnsflsbmKng2_C0huR-g8'
yt = YouTubeDataAPI(api_key)

results = yt.search('bridge2rwanda')
print(results)
