import requests
import pyyoutube

from youtube_api import YouTubeDataAPI

api_key = 'AIzaSyC8ScUbhEYWOFOnsflsbmKng2_C0huR-g8'
yt = YouTubeDataAPI(api_key)

results = yt.search('bridge2rwanda')
print(results)

"""

from pyyoutube import Api
api = Api(api_key="AIzaSyC8ScUbhEYWOFOnsflsbmKng2_C0huR-g8")

from youtube_videos.py import youtube_search
import json

test = youtube_search("spinners")
test



# Get authorization url
>>> api.get_authorization_url()
('https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=id&redirect_uri=https%3A%2F%2Flocalhost%2F&scope=scope&state=PyYouTube&access_type=offline&prompt=select_account', 'PyYouTube')
# user to do
# copy the response url
>>> api.generate_access_token(authorization_response="link for response")
AccessToken(access_token='token', expires_in=3599, token_type='Bearer')



>>> video_by_id = api.get_video_by_id(video_id="CvTApw9X8aA")

>>> video_by_id
VideoListResponse(kind='youtube#videoListResponse')

>>> video_by_id.items
[Video(kind='youtube#video', id='CvTApw9X8aA')]

"""