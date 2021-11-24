import boto3
import json


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('usersTable')
    email = event["email"]
    name = event["name"]
    comment = event["comment"]
    response = table.put_item(Item={"email": email, "name": name, "comment": comment})
    return {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'statusCode': 200,
        'body': json.dumps(response)
    }
