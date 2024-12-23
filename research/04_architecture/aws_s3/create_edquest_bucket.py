import boto3
from botocore.exceptions import ClientError

DEFAULT_REGION = "us-east-1"

def create_s3_bucket(config):
    bucket_name = config["bucket_name"]
    region_name = config.get("region", DEFAULT_REGION)
    directories = config["directory_list"]
    print(f"bucket_name --- ", bucket_name)
    print(f"region --- ", region_name)
    print(f"directories --- ", directories)
    try:
        s3_client = boto3.client("s3", region_name=region_name)
         # Check if the bucket exists
        if not bucket_exists(s3_client, bucket_name):
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})
            print("Bucket created successfully ---------")
        else:
            print("Bucket already exists ---------")

        print("Bucket created successfuly ---------")
        # create_directory(directories, s3_client, bucket_name)
        check_and_create_directory(directories, s3_client, bucket_name)

        print("directories created successfuly **********")
    except ClientError as e:
        print(f"Failed to create bucket: {e}")
        raise

def bucket_exists(s3_client, bucket_name):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        # Check if the error is 404 (bucket does not exist)
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            return False
        raise

def check_and_create_directory(directories, s3_client, bucket_name):
    # Check if the directory exists, if not, create it
    for directory in directories:
        # Check if directory exists by listing objects with the directory prefix
        result = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=directory, MaxKeys=1)
        
        if 'Contents' not in result:
            # If no objects are found, create the directory by uploading an empty object
            try:
                s3_client.put_object(Bucket=bucket_name, Key=directory + '/')
                print(f"Directory {directory} created successfully in bucket {bucket_name}.")
            except Exception as e:
                print(f"Error creating directory {directory}: {e}")
        else:
            print(f"Directory {directory} already exists in bucket {bucket_name}.")

# def create_directory(directories, s3_client, bucket_name):
#     # Create the directories in the bucket
#     for directory in directories:
#         try:
#             # Adding an empty object to represent the directory
#             s3_client.put_object(Bucket=bucket_name, Key=directory)
#             print(f"Directory {directory} created successfully in bucket {bucket_name}.")
#         except Exception as e:
#             print(f"Error creating directory {directory}: {e}")