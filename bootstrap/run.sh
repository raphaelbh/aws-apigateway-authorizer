#!/bin/bash
set -e

echo "#################################### BOOTSTRAP ####################################"

echo -ne "===> Setting up local aws account"
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID > /dev/null
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY > /dev/null
aws configure set region $AWS_DEFAULT_REGION > /dev/null
echo "... Done"

echo -ne "===> Creating resources"
aws cloudformation create-stack --stack-name demo-authorizer --template-body file://template.yaml > /dev/null
aws cloudformation wait stack-create-complete --stack-name demo-authorizer > /dev/null
echo "... Done"

echo "#################################### BOOTSTRAP ####################################"