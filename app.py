import requests

response = requests.get('https://api.jikan.moe/v4/anime')
print(response.status_code)
print(response.json())

title = response.json()['data'][0]['url']
print(f'{title}')

print('What type of ')