import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    """
    Check if an S3 bucket exists by listing buckets and create it if not.
    
    Args:
    - bucket_name: The name of the bucket to create.
    - region: The AWS region for the bucket (e.g., 'us-east-1').
    
    Returns:
    - str: Message indicating the result.
    """
    print(f"bucket_name : {bucket_name}")
    print(f"region : {region}")
    s3_client = boto3.client('s3', region_name=region)
    s3_client.create_bucket(Bucket=bucket_name)