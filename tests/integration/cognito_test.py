import unittest
import uuid
import os
import requests
import application.cognito as cognito
from dotenv import load_dotenv

load_dotenv()
API_URL=os.environ.get("API_URL")

class CognitoTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(CognitoTest, cls).setUpClass()
        cls.user = cls._create_user()

    def test_1_sign_up_user(self):
        response_sign_up = cognito.sign_up(self.user)
        response_admin_confirm_sign_up = cognito.admin_confirm_sign_up(self.user)
        assert 200 == response_sign_up['statusCode']
        assert 200 == response_admin_confirm_sign_up['statusCode']

    def test_2_authorizer_empty_token(self):
        response = requests.get(API_URL)
        assert 401 == response.status_code


    def test_3_authorizer_invalid_token(self):
        headers = {'Authorization' : 'Bearer invalid_access_token'}
        response = requests.get(API_URL, headers=headers)
        assert 401 == response.status_code
    
    def test_4_authorizer_valid_token(self):
        jwt = cognito.initiate_auth(self.user)
        access_token = jwt['body']['access_token']
        headers = {'Authorization' : 'Bearer ' + access_token}
        response = requests.get(API_URL, headers=headers)
        assert 200 == response.status_code

    def test_5_delete_user(self):
        response_initiate_auth = cognito.initiate_auth(self.user)
        access_token = response_initiate_auth['body']['access_token']
        response_delete_user = cognito.delete_user(access_token)
        assert 200 == response_initiate_auth['statusCode']
        assert 200 == response_delete_user['statusCode']


    def _create_user():
        user = uuid.uuid4().hex[0:7]
        email = user + '@fake.com'
        return {
            'username':  email,
            'password': 'Mudar@123',
            'attributes': [{
                'Name': 'name',
                'Value': user
            }, {
                'Name': 'email',
                'Value': email
            }]
        }

if __name__ == '__main__':
    unittest.main()