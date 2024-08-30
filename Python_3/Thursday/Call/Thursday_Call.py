#%%

# list S3 buckets

import boto3

#%%

response = s3.list_buckets()

#%%

buckets = response["Buckets"]

#%%

for bucket in buckets: 
    print(bucket['name'])
