import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    """
    Check if an S3 bucket exists, and create it if not.
    
    Args:
    - bucket_name: The name of the bucket to create.
    - region: The AWS region for the bucket (e.g., 'us-east-1').
    
    Returns:
    - str: Message indicating the result.
    """
    s3_client = boto3.client('s3', region_name=region)
    
    # Check if bucket exists
    try:
        response = s3_client.head_bucket(Bucket=bucket_name)
        return f"Bucket '{bucket_name}' already exists."
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            # Bucket does not exist, proceed to create it
            try:
                if region:
                    s3_client.create_bucket(
                        Bucket=bucket_name,
                        CreateBucketConfiguration={'LocationConstraint': region}
                    )
                else:
                    s3_client.create_bucket(Bucket=bucket_name)  # Default region
                return f"Bucket '{bucket_name}' created successfully in region '{region or 'us-east-1'}'."
            except ClientError as create_error:
                return f"Failed to create bucket: {create_error}"
        else:
            return f"Error checking bucket existence: {e}"

# # Example usage
# if __name__ == "__main__":
#     bucket_name = "my-unique-bucket-name-12345"  # Replace with your bucket name
#     region = "us-east-1"  # Replace with your desired region or leave None for default region
#     result = create_s3_bucket(bucket_name, region)
#     print(result)
