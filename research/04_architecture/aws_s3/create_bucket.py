import boto3
from botocore.exceptions import ClientError

# bucket_name = "my-edquest-bucket-name-1"  # Replace with a unique bucket name
# region = "${{ secrets.AWS_REGION }}"  # Replace with your region or use GitHub Secrets

def create_s3_bucket(bucket_name, region='us-east-1'):
    print(f"bucket_name --- ", bucket_name)
    print(f"region --- ", region)
    try:
        s3_client = boto3.client("s3", region_name=region)
        s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        print(f"Failed to create bucket: {e}")
        raise

create_s3_bucket(bucket_name)