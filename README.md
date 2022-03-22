# AWS API Authorizer + Cognito

[![Project Status](https://img.shields.io/static/v1?label=project%20status&message=complete&color=success&style=flat-square)](#)

Proof of concept to demonstrate how to create a API Authorizer with Cognito.

Tech Stack:
- ApiGateway
- Cognito
- JWT


## Requirements

[![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)


## Installation

Update `docker-compose.yaml` with the correct env variables: 
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`

```bash
$ (cd bootstrap && docker-compose up)
```

 
## Usage

Set the follow env variables (application/.env)  
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `USER_POOL_ID`
- `USER_POOL_CLIENT_ID`

Getting access token

```python
import application.cognito as cognito

user = {
    'username': 'raphaeldias.ti@gmail.com',
    'password': 'Mudar@123'
}

jwt = cognito.initiate_auth(user)
access_token = jwt['body']['access_token'] 
```

Requesting api

```python
import requests

headers = {'Authorization' : 'Bearer ' + $access_token}
response = requests.get($API_URL, headers=headers)
```


## Running Tests

Set the follow env variables (tests/.env)  
- `API_URL`

```bash
$ export PYTHONPATH=application 
$ pytest --cache-clear tests/
```

## Tech Stack

[![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![aws](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)


## Reference

- https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html


## Feedback


If you have any feedback, please contact me at raphaeldias.ti@gmail.com

[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/raphaelbh)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raphaelbh/)