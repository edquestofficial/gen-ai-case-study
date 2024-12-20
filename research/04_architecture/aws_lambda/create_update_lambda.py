import boto3
import zipfile
import os
import json

AWS_REGION = "us-east-1"
LAMBDA_FUNCTION_NAME = "MyLambdaFunction"
ROLE_NAME = "LambdaExecutionRole"
POLICY_NAME = "LambdaBasicPolicy"
ZIP_FILE_NAME = "post_call_analysis.zip"

# Initialize AWS clients
iam_client = boto3.client('iam', region_name=AWS_REGION)
lambda_client = boto3.client('lambda', region_name=AWS_REGION)

# Specify the directory where the post_call_analysis.py resides
LAMBDA_CODE_DIR = "/functions"  # Update this path accordingly

def create_or_update_lambda_function(role_arn):
    """Create or update the Lambda function."""
    # Package the Lambda code
    with zipfile.ZipFile(ZIP_FILE_NAME, 'w') as zf:
        file_path = os.path.join(LAMBDA_CODE_DIR, "post_call_analysis.py")
        zf.write(file_path, arcname="post_call_analysis.py")  # Use arcname to control the file name inside the ZIP
        # zf.write('post_call_analysis.py')  # Ensure your Lambda handler is in the same directory

    # Check if Lambda function exists
    try:
        response = lambda_client.get_function(FunctionName=LAMBDA_FUNCTION_NAME)
        print(f"Updating existing Lambda function: {LAMBDA_FUNCTION_NAME}")

        # Update function code
        lambda_client.update_function_code(
            FunctionName=LAMBDA_FUNCTION_NAME,
            ZipFile=open(ZIP_FILE_NAME, 'rb').read()
        )
    except lambda_client.exceptions.ResourceNotFoundException:
        print(f"Creating new Lambda function: {LAMBDA_FUNCTION_NAME}")

        # Create new Lambda function
        lambda_client.create_function(
            FunctionName=LAMBDA_FUNCTION_NAME,
            Runtime="python3.9",
            Role=role_arn,
            Handler="lambda_function.lambda_handler",
            Code={"ZipFile": open(ZIP_FILE_NAME, 'rb').read()},
            Timeout=15,
            MemorySize=128
        )

    print(f"Lambda function {LAMBDA_FUNCTION_NAME} is ready!")