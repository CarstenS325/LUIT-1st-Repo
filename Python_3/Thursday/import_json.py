import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # TODO implement 
    print('Hello form Lambda!')

    response - s3.list_buckets()

    bucket_names = []
    buckets = response['Buckets']

    return {
        'body':  json.dumps(bucket_names)
    }
