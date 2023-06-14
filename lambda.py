import json
import boto3
dynamodb = boto3. resource('dynamodb')
table = dynamodb.Table('Registration_T')

def lambda_handler(event, context):
    response = table.put_item(
        Item={
            'email' : event['email'],
            'name' : event['name'],
            'phone' : event['phone'],
            'passwprd' : event['password']
        }
    )

    return {
        'statusCode' : 200,
        'headers' : {
            'Content-Type' : 'application/json',
            'Access-Control-Allow-Origin' : '*'
        },
        'body' : json.dumps({'message' : 'Registration Successfull '})
    }