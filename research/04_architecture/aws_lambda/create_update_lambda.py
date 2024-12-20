import boto3
import zipfile
import os
import json

AWS_REGION = "us-east-1"
LAMBDA_FUNCTION_NAME = "MyLambdaFunction"
ROLE_NAME = "LambdaExecutionRole"
POLICY_NAME = "LambdaBasicPolicy"
LAMBDA_CODE_DIR = "/functions"  # Update this path accordingly
ZIP_FILE_NAME = "post_call_analysis.zip"

# Initialize AWS clients
iam_client = boto3.client('iam', region_name=AWS_REGION)
lambda_client = boto3.client('lambda', region_name=AWS_REGION)

# Specify the directory where the post_call_analysis.py resides

def create_or_update_lambda_function(role_arn):
    """Create or update the Lambda function."""
    # Package the Lambda code
    file_name = "post_call_analysis.py" 
    # file_path = os.path.join(LAMBDA_CODE_DIR, file_name)

    current_file_path = os.path.abspath(__file__)  # Path to the executing script
    # Navigate to the desired directory relative to the script
    base_directory = os.path.dirname(current_file_path)  # Current script's directory
    lambda_functions_dir = os.path.join(base_directory, "functions")  # Target directory

    # Construct the full path to the Lambda function file
    file_path = os.path.join(lambda_functions_dir, "post_call_analysis.py")


    # research\04_architecture\aws_lambda\functions\post_call_analysis.py
    # /home/runner/work/gen-ai-case-study/gen-ai-case-study/functions/post_call_analysis.py

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}. Please verify the path and filename.")

    # Package the Lambda function into a ZIP file
    with zipfile.ZipFile(ZIP_FILE_NAME, 'w') as zf:
        zf.write(file_path, arcname=file_name)  # Use arcname to control the filename inside the ZIP

    print(f"Packaged {file_path} into {ZIP_FILE_NAME}")

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