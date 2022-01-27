import boto3
import sys
import os
from dotenv import load_dotenv

class Cognito:

    def __init__(self):
        load_dotenv()
        self.AWS_REGION = os.environ.get("AWS_REGION")
        self.USER_POOL_ID = os.environ.get("USER_POOL_ID")
        self.USER_POOL_CLIENT_ID = os.environ.get("USER_POOL_CLIENT_ID")
        self.cidp = boto3.client('cognito-idp', region_name=self.AWS_REGION)
    
    def sign_up(self, user):
        try:
            response = self.cidp.sign_up(
                ClientId = self.USER_POOL_CLIENT_ID,
                Username = user['username'],
                Password = user['password'],
                UserAttributes = user['attributes']
            )
            return self.__response(200, {
                'userSub': response['UserSub'],
                'codeDeliveryDetails': response['CodeDeliveryDetails'],
                'userConfirmed': response['UserConfirmed']
            })
        except:
            e = sys.exc_info()[1]
            return self.__response(500, e.args[0])
        
    def admin_confirm_sign_up(self, user):
        try:
            self.cidp.admin_confirm_sign_up(
                UserPoolId = self.USER_POOL_ID,
                Username = user['username']
            )
            return self.__response(200, {
                'userConfirmed': True
            })
        except:
            e = sys.exc_info()[1]
            return self.__response(500, e.args[0])

    def initiate_auth(self, user):
        try:
            response = self.cidp.initiate_auth(
                AuthFlow = 'USER_PASSWORD_AUTH',
                AuthParameters = {
                    'USERNAME': user['username'],
                    'PASSWORD': user['password']
                },
                ClientId = self.USER_POOL_CLIENT_ID
            )
            return self.__response(200, {
                'access_token': response['AuthenticationResult']['AccessToken'],
                'id_token': response['AuthenticationResult']['IdToken'],
                'refresh_token': response['AuthenticationResult']['RefreshToken']
            })
        except:
            e = sys.exc_info()[1]
            return self.__response(500, e.args[0])

    def get_user(self, access_token):
        try:
            response = self.cidp.get_user(
                AccessToken = access_token
            )
            return self.__response(200, response['UserAttributes'])
        except:
            e = sys.exc_info()[1]
            return self.__response(500, e.args[0])

    def delete_user(self, access_token):
        try:
            self.cidp.delete_user(
                AccessToken = access_token
            )
            return self.__response(200, {
                'userDeleted': True
            })
        except:
            e = sys.exc_info()[1]
            return self.__response(500, e.args[0])

    def global_sign_out(self, access_token):
        try:
            response = self.cidp.global_sign_out(
                AccessToken = access_token
            )
            return self.__response(200, response)
        except:
            e = sys.exc_info()[1]
            return self.__response(500, e.args[0])

    def __response(self, statusCode, body):
        response = {
            'statusCode': statusCode,
            'body': body
        }
        return response

cognito = Cognito()