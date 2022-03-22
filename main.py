import requests
import os

OKTA_URL = os.environ['OKTA_URL']
OKTA_API_KEY = os.environ['OKTA_API_KEY']

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f"SSWS {OKTA_API_KEY}",
}

def pagination_value(response):
    after_link = response.headers['link'].split(',', 1)[1]
    after_curser = after_link.split('after=')[1].split('&')[0]
    return after_curser

response = requests.get(f'https://{OKTA_URL}/api/v1/users', headers=headers)
user_list = response.json()
next_page = pagination_value(response)

# Pagination
while len(user_list) >= 200:
    next_response = requests.get(f'https://{OKTA_URL}/api/v1/users?after={next_page}', headers=headers)
    next_list = next_response.json()
    user_list.extend(next_list)
    if len(next_list) < 200:
        break
    next_page = pagination_value(next_response)
    
print("Total Users: " + str(len(user_list)))
    
for i in user_list:
    user_id=i['id']
    user_email=i['profile']['email']
    print(f"User emai:{user_email} ID: {user_id}")
    expire_pw_response = requests.post(f'https://{OKTA_URL}/api/v1/users/{user_id}/lifecycle/expire_password', headers=headers)
    print(f"pw expired respnse: {expire_pw_response}")
    expire_session_response = requests.delete(f'https://{OKTA_URL}/api/v1/users/{user_id}/sessions', headers=headers)
    print(f"session expire response: {expire_session_response}")
