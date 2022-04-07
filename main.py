# Copyright 2022 Ada Health GmbH

import requests
import os

OKTA_URL = 'https://' + os.environ['OKTA_URL']
OKTA_API_KEY = os.environ['OKTA_API_KEY']

headers = {
    'Accept': 'application/json',
    'Authorization': f"SSWS {OKTA_API_KEY}",
}
session = requests.Session()
session.headers.update(headers)

url = f'{OKTA_URL}/api/v1/users'
while url:
    response = session.get(url)
    users = response.json()
    for user in users:
        user_id = user['id']
        user_email = user['profile']['email']
        print(f"User email: {user_email} ID: {user_id}")
        expire_pw_response = session.post(f'{OKTA_URL}/api/v1/users/{user_id}/lifecycle/expire_password')
        print(f"pw expired response: {expire_pw_response}")
        expire_session_response = session.delete(f'{OKTA_URL}/api/v1/users/{user_id}/sessions')
        print(f"session expire response: {expire_session_response}")
    next = response.links.get('next')
    url = next['url'] if next else None
