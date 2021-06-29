import requests

sample_text = input('Enter a text: ')

url = 'http://text-processing.com/api/sentiment/'
myobj = {'text': sample_text}

response = requests.post(url, data = myobj)

print(response.json())