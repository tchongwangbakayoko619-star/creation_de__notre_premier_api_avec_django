import requests

endpoint = 'http://localhost:8000/api/?q=tchongwang=python&age=22'

response = requests.get(endpoint)

print(response.json())
print(response.status_code)