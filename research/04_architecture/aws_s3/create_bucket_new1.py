import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region='us-east-1'):
    """
    Create an S3 bucket in the specified region. Handles region-specific constraints.
    """
    print(f"Region: {region}")
    print(f"Bucket Name: {bucket_name}")
    
    try:
        # Create S3 client for the specified region
        s3_client = boto3.client("s3", region_name=region)
        
        # Handle region-specific bucket creation
        if region != "us-east-1":
            # Add LocationConstraint for non-us-east-1 regions
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        else:
            # No LocationConstraint required for us-east-1
            s3_client.create_bucket(Bucket=bucket_name)

        print(f"Bucket '{bucket_name}' created successfully in region '{region}'.")
    except ClientError as e:
        print(f"Failed to create bucket: {e}")
        raise

# # Example usage
# if __name__ == "__main__":
#     bucket_name = "my-unique-bucket-name-12345"  # Replace with your bucket name
#     region = "us-west-2"  # Replace with your desired region
#     create_s3_bucket(bucket_name, region)
