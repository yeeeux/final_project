import requests
import json

url = 'http://localhost:8080'
param_dict = {'param': 'data'}
response = (requests.get(url)).json()
# response = requests.post(url, data=json.dumps(param_dict))
print(response['username'])