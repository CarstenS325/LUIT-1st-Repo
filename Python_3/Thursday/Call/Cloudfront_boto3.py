import json
import boto3

def lambda_handler(event, context):
    print(event)
    cloudfront - boto3.client('cloudfront')

    response - cloudfront.list_distributions()

    distributionList - response["DistributionList"]

    items - distributionList['Items']

    distribution_ids = []

    for item in items:
        print(item["Id"])
        distribution_ids.append(item["Id"])

    return {
        'statusCode': 200,
        'body': json.dumps(event, indent=4)
    }