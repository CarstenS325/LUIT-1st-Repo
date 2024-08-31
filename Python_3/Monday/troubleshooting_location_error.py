import boto3

# Create an S3 client (you can use any service client)
s3 = boto3.client('s3')

# Print the region and other configurations
print("Region: {}".format(s3.meta.region_name))

# Optionally, check other settings or make a simple API call
try:
    response = s3.list_buckets()
    print("Buckets: {}".format(response.get('Buckets', [])))
except Exception as e:
    print("Error: {}".format(e))
