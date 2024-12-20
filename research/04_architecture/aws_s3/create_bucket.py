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
    s3_client = boto3.client('s3', region_name=region)
    
    # List all buckets and check for the bucket name
    try:
        buckets = s3_client.list_buckets()
        bucket_names = [bucket['Name'] for bucket in buckets['Buckets']]
        if bucket_name in bucket_names:
            print(f"Bucket '{bucket_name}' already exists.")
    except ClientError as e:
        print(f"Error listing buckets: {e}")

    # Proceed to create the bucket
    try:
        if region and region != "us-east-1":
            s3_client.create_bucket(
                Bucket=bucket_name,
                # CreateBucketConfiguration={'LocationConstraint': region}
            )
        else:
            s3_client.create_bucket(Bucket=bucket_name)  # Default region (us-east-1)
        print(f"Bucket '{bucket_name}' created successfully in region '{region or 'us-east-1'}'.")
    except ClientError as create_error:
        print(f"Failed to create bucket: {create_error}")
