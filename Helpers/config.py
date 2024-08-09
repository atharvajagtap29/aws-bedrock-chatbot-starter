# CONFIGURATION MODULE FOR AWS CREDENTIALS

import boto3

def create_client(service, region_name='us-east-1'):
    session = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key=''
    )

    return session.client(service, region_name)
