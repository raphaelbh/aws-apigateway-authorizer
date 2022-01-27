import uuid
class Fake:
    def create_user(self):
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

fake = Fake()