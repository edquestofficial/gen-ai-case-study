import boto3
import zipfile
import os
import json

AWS_REGION = "us-east-1"
LAMBDA_FUNCTION_NAME = "PostCallAnalysis"
ROLE_NAME = "LambdaExecutionRole"
POLICY_NAME = "LambdaBasicPolicy"
LAMBDA_CODE_DIR = "/functions"  # Update this path accordingly
ZIP_FILE_NAME = "post_call_analysis.zip"
S3_BUCKET_NAME = "my-edquest-bucket-name-1111"  # Replace with your S3 bucket name
S3_EVENT = "s3:ObjectCreated:*"  # Event to trigger Lambda function on object creation

# Initialize AWS clients
iam_client = boto3.client('iam', region_name=AWS_REGION)
lambda_client = boto3.client('lambda', region_name=AWS_REGION)
s3_client = boto3.client('s3', region_name=AWS_REGION)

def get_aws_account_id():
    """Retrieve the AWS account ID from the environment variables."""
    sts_client = boto3.client('sts')
    account_id = sts_client.get_caller_identity()["Account"]
    return account_id

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
            Handler="post_call_analysis.lambda_handler",
            Code={"ZipFile": open(ZIP_FILE_NAME, 'rb').read()},
            Timeout=15,
            MemorySize=128
        )

    print(f"Lambda function {LAMBDA_FUNCTION_NAME} is ready!")

    # Add S3 trigger to Lambda function
    add_s3_trigger_to_lambda()

def add_s3_trigger_to_lambda():
    """Add an S3 trigger to the Lambda function."""
    try:
        # Get the AWS Account ID
        aws_account_id = get_aws_account_id()
        # Grant the Lambda function permission to be triggered by the S3 bucket
        lambda_client.add_permission(
            FunctionName=LAMBDA_FUNCTION_NAME,
            StatementId="S3TriggerPermission",  # Unique ID for this permission
            Action="lambda:InvokeFunction",
            Principal="s3.amazonaws.com",
            SourceArn=f"arn:aws:s3:::{S3_BUCKET_NAME}/audio/",
        )
        print(f"Permission granted to trigger {LAMBDA_FUNCTION_NAME} from S3 bucket {S3_BUCKET_NAME}")

        # Add S3 bucket notification to trigger Lambda on object creation
        s3_client.put_bucket_notification_configuration(
            Bucket=S3_BUCKET_NAME,
            NotificationConfiguration={
                'LambdaFunctionConfigurations': [
                    {
                        'LambdaFunctionArn': f"arn:aws:lambda:{AWS_REGION}:{aws_account_id}:function:{LAMBDA_FUNCTION_NAME}",
                        'Events': [S3_EVENT],  # Specify the event you want to trigger the Lambda function
                        "Filter": {
                            "Key": {
                                "FilterRules": [
                                    {"Name": "prefix", "Value": ""},
                                    {"Name": "suffix", "Value": "*.mp3"}
                                ]
                            }
                        }
                    },
                ],
            },
        )
        print(f"S3 trigger added for Lambda function {LAMBDA_FUNCTION_NAME} on events: {S3_EVENT}")

    except Exception as e:
        print(f"Error adding S3 trigger: {str(e)}")

# You may also need to update the IAM policy for your Lambda function's role
# to allow S3 actions (like "s3:GetObject") if it will interact with objects.