import os
import requests
from libs.fake import fake
from libs.cognito import cognito
from dotenv import load_dotenv

load_dotenv()
API_URL = os.environ.get("API_URL")

# fake user
user = fake.create_user()

# sign up user
cognito.sign_up(user)
cognito.admin_confirm_sign_up(user)

# check authorizer - empty token (no headers)
response = requests.get(API_URL)
print('expected: 401 (Unauthorized)')
print('current: ' + str(response.status_code))

# check authorizer - valid token
jwt = cognito.initiate_auth(user)
access_token = jwt['body']['access_token']
headers = {'Authorization' : 'Bearer ' + access_token}
response = requests.get(API_URL, headers=headers)
print('expected: 200 (Success)')
print('current: ' + str(response.status_code))

# delete user
jwt = cognito.initiate_auth(user)
access_token = jwt['body']['access_token']
cognito.delete_user(access_token)