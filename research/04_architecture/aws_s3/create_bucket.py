import boto3
from botocore.exceptions import ClientError

# bucket_name = "my-edquest-bucket-name-1"  # Replace with a unique bucket name
# region = "${{ secrets.AWS_REGION }}"  # Replace with your region or use GitHub Secrets

def create_s3_bucket(bucket_name, region='us-east-1'):
    print(f"bucket_name --- ", bucket_name)
    print(f"region --- ", region)
    directories = ['audio/', 'audio-to-text/', 'output-summary/']
    try:
        s3_client = boto3.client("s3", region_name=region)
        s3_client.create_bucket(Bucket=bucket_name)
        print("Bucket created successfuly ---------")
        create_directory(directories, s3_client, bucket_name)

        print("directories created successfuly **********")
    except ClientError as e:
        print(f"Failed to create bucket: {e}")
        raise

def create_directory(directories, s3_client, bucket_name):
    # Create the directories in the bucket
    for directory in directories:
        try:
            # Adding an empty object to represent the directory
            s3_client.put_object(Bucket=bucket_name, Key=directory)
            print(f"Directory {directory} created successfully in bucket {bucket_name}.")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")

# create_s3_bucket(bucket_name)