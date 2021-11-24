import json
import logging
import boto3
from botocore.exceptions import ClientError

from botocore.client import Config


def create_presigned_post(bucket_name, object_name,
                          fields=None, conditions=None, expiration=3600):
    s3_client = boto3.client('s3', region_name='ap-southeast-1', config=Config(signature_version='s3v4'))
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,

                                                     #  Conditions=[
                                                     #  ["eq", "$success_action_redirect", "www.google.com"],
                                                     #     {"success_action_status": "200"}],
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    return response


def lambda_handler(event, context):
    import uuid
    name = str(uuid.uuid4())
    ext = event["queryStringParameters"]['extension']
    key = f'{name}.{ext}'
    response = create_presigned_post('cv-maker', key)
    return {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'statusCode': 200,
        'body': json.dumps(response)
    }
