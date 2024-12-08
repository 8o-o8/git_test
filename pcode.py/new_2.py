import requests

url = 'https://random-d.uk/api/random'
res = requests.get(url)
print(res.json())
