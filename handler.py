import boto3
import json


def lambda_handler(event, context):
    """
    AWS Lambda function to add user comments to a DynamoDB table.

    Args:
        event (dict): The event that triggered the Lambda function.  Must contain "email", "name", and "comment" keys.
        context (object): The Lambda context object.

    Returns:
        dict: A dictionary containing the HTTP response headers, status code, and the DynamoDB put_item response.
              Returns a 200 status code on success.  Error handling is minimal; robust error handling should be added for production.
    """
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('usersTable')
    email = event["email"]
    name = event["name"]
    comment = event["comment"]
    response = table.put_item(Item={"email": email, "name": name, "comment": comment})
    return {
        'headers': {
            "Access-Control-Allow-Origin": "*", # Allows requests from any origin
            "Access-Control-Allow-Methods": "*" # Allows all HTTP methods
        },
        'statusCode': 200,
        'body': json.dumps(response)
    }

