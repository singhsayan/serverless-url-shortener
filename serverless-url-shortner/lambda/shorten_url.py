import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener-table')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    original_url = body.get('url')
    slug = str(uuid.uuid4())[:6]
    
    table.put_item(Item={'slug': slug, 'url': original_url})

    return {
        'statusCode': 200,
        'body': json.dumps({'short_url': f"{event['headers']['host']}/{slug}"})
    }
