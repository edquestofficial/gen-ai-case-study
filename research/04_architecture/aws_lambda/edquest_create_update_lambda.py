import boto3
import zipfile
import os
import json
import uuid

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.config import CONFIG

lambda_config = CONFIG["Audio_To_Transcript"]["lambda"]
AWS_REGION = lambda_config["REGION_NAME"]
LAMBDA_FUNCTION_NAME = lambda_config["LAMBDA_FUNCTION_NAME"]
ROLE_NAME = lambda_config["ROLE_NAME"]
POLICY_NAME = lambda_config["POLICY_NAME"]
LAMBDA_CODE_DIR = lambda_config["LAMBDA_CODE_DIR"]
ZIP_FILE_NAME = lambda_config["ZIP_FILE_NAME"]
S3_BUCKET_NAME = lambda_config["BUCKET_NAME"]
S3_EVENT = lambda_config["S3_EVENT"]
# print(AWS_REGION)

# Initialize AWS clients
lambda_client = boto3.client('lambda', region_name=AWS_REGION)
FILE_NAME = "edquest_post_call_analysis.py"

# Specify the directory where the post_call_analysis.py resides

def create_or_update_lambda_function(role_arn):
    print("Execute the lambda function")
    """Create or update the Lambda function."""
    # Package the Lambda code
    file_name = FILE_NAME 

    current_file_path = os.path.abspath(__file__)  # Path to the executing script
    # Navigate to the desired directory relative to the script
    base_directory = os.path.dirname(current_file_path)  # Current script's directory
    lambda_functions_dir = os.path.join(base_directory, "functions")  # Target directory

    # Construct the full path to the Lambda function file
    file_path = os.path.join(lambda_functions_dir, FILE_NAME)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}. Please verify the path and filename.")

    # Package the Lambda function into a ZIP file
    with zipfile.ZipFile(ZIP_FILE_NAME, 'w') as zf:
        zf.write(file_path, arcname=file_name)  # Use arcname to control the filename inside the ZIP

    print(f"Packaged {file_path} into {ZIP_FILE_NAME}")

    # Check if Lambda function exists
    try:
        print("response-----------1111")
        response = lambda_client.get_function(FunctionName=LAMBDA_FUNCTION_NAME)
        status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        print(status_code)

        if status_code == 200 :
            print("Lambda function creation response ----- ", response)
             # Update function code
            # lambda_client.update_function_code(
            #     FunctionName=LAMBDA_FUNCTION_NAME,
            #     ZipFile=open(ZIP_FILE_NAME, 'rb').read()
            # )
        else:
            print("New Lambda function is create ----- ", )

        print(f"Updating existing Lambda function: {LAMBDA_FUNCTION_NAME}")

       
    except lambda_client.exceptions.ResourceNotFoundException:
        # print(f"Creating new Lambda function: {LAMBDA_FUNCTION_NAME}")
        # print(f"Exceptions:=== {lambda_client}")
        # print(f"Exceptions:=== {lambda_client.exceptions}")
        # print(f"Exceptions:=== {lambda_client.exceptions.ResourceNotFoundException}")

        # Create new Lambda function
        lambda_client.create_function(
            FunctionName=LAMBDA_FUNCTION_NAME,
            Runtime="python3.9",
            Role=role_arn,
            Handler="edquest_post_call_analysis.lambda_handler",
            Code={"ZipFile": open(ZIP_FILE_NAME, 'rb').read()},
            Timeout=15,
            MemorySize=128
        )

    print(f"Lambda function {LAMBDA_FUNCTION_NAME} is ready!")


# You may also need to update the IAM policy for your Lambda function's role
# to allow S3 actions (like "s3:GetObject") if it will interact with objects.