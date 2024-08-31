import boto3

# Create an S3 client
s3 = boto3.client('s3')  # Region is picked up from configuration files

# Test bucket creation
try:
    response = s3.create_bucket(
        Bucket='boto3-testing-08312024',
        CreateBucketConfiguration={
            'LocationConstraint': s3.meta.region_name  # Use the region from the client
        }
    )
    print("Bucket created:", response)
except Exception as e:
    print("Error:", e)
