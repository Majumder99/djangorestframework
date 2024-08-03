import requests

endpoint = 'http://localhost:8000/api/views'

get_response = requests.post(endpoint, json={ "title": "This is a title" })
# print(get_response.status_code)
# print(get_response.text)
print(get_response.json())