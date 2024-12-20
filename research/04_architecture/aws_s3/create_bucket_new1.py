import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region='us-east-1'):
    """
    Create an S3 bucket in the specified region. Handles us-east-1 correctly.

    Args:
        bucket_name (str): Name of the bucket to create.
        region (str): AWS region for the bucket.

    Returns:
        None
    """
    try:
        # Initialize the S3 client
        s3_client = boto3.client("s3", region_name=region)

        # us-east-1 specific handling: omit LocationConstraint
        if region == "us-east-1":
            response = s3_client.create_bucket(Bucket=bucket_name)
        else:
            response = s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )

        print(f"Bucket '{bucket_name}' created successfully in region '{region}'.")
        return response

    except ClientError as e:
        print(f"Failed to create bucket: {e}")
        raise

# # Example usage
# if __name__ == "__main__":
#     bucket_name = "my-unique-bucket-name-12345"  # Replace with a unique bucket name
#     region = "us-east-1"  # Specify your desired region
#     create_s3_bucket(bucket_name, region)
