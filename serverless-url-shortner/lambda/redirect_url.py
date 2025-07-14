import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener-table')

def lambda_handler(event, context):
    slug = event['pathParameters']['slug']
    
    response = table.get_item(Key={'slug': slug})
    item = response.get('Item')

    if item:
        return {
            'statusCode': 302,
            'headers': {
                'Location': item['url']
            }
        }
    else:
        return {
            'statusCode': 404,
            'body': 'Not Found'
        }
