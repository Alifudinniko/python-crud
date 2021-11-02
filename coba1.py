import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

# print(response)

# print(response.json())

# print(response.json()['items'])

# for data in response.json()['items']:
#     print(data['title'])
#     print(data['link'])
#     print()

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
        print()
    else:
        print('pass')
        print()
