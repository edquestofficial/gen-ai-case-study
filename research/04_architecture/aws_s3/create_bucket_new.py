import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import sys

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

def create_s3_bucket(bucket_name, region='us-east-1'):
    try:
        # Check if the bucket already exists by listing all buckets
        existing_buckets = s3.list_buckets()
        bucket_names = [bucket['Name'] for bucket in existing_buckets['Buckets']]
        
        if bucket_name in bucket_names:
            print(f"Bucket {bucket_name} already exists. Exiting.")
            sys.exit(0)  # Exit if the bucket already exists

        # Create a new bucket if it doesn't exist
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket {bucket_name} created successfully in region {region}.")
        
    except s3.exceptions.BucketAlreadyExists as e:
        print(f"Error: Bucket {bucket_name} already exists. Please choose a different name.")
        sys.exit(0)
    except s3.exceptions.BucketAlreadyOwnedByYou as e:
        print(f"Error: Bucket {bucket_name} is already owned by you.")
        sys.exit(0)
    except NoCredentialsError:
        print("Error: No AWS credentials found. Please configure your credentials.")
        sys.exit(1)
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials. Please check your configuration.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

# # Example usage
# bucket_name = "my-unique-bucket-name-1234"  # Make sure the name is globally unique
# region = "us-west-2"  # Specify the region, or use 'us-east-1' by default
# create_s3_bucket(bucket_name, region)
