import requests
url = 'http://127.0.0.1:8000/api/'

response_code = requests.get(url)

print(response_code.json())