import boto3
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('boto3')
logger.setLevel(logging.DEBUG)

# Create an S3 client
s3 = boto3.client('s3')

# Test bucket creation
try:
    response = s3.create_bucket(
        Bucket='boto3-testing-08312024'
           )
    print("Bucket created:", response)
except Exception as e:
    print("Error:", e)