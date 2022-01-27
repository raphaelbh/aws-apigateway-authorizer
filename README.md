# AWS Cognito

## Overview

**ApiGateway**
Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale. API developers can create APIs that access AWS or other web services, as well as data stored in the AWS Cloud.

https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html

**Cognito / Authorizer**
Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, Google or Apple.

https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html

**JWT**
JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. 

https://jwt.io/introduction

## Use Case
- Request without access token
- Request with valid acess token

## Requirements
- aws account (https://aws.amazon.com/)
- python (https://www.python.org/)

## Setup
1. Create stack through cloud formation file (cloudformation/stack.yml)

2. Set the follow env variables (app/libs/.env) 
- AWS_ACCESS_KEY_ID=XXXX
- AWS_SECRET_ACCESS_KEY=XXXX
- AWS_REGION=XXXX
- USER_POOL_ID=XXXX
- APP_CLIENT_ID=XXXX
- API_URL=XXXX

## Running

`$ python3 ./app/main.py`