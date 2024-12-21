import boto3
import json

AWS_REGION = "us-east-1"
ROLE_NAME = "LambdaExecutionRole"
POLICY_NAME = "LambdaBasicPolicy"

# Initialize AWS clients
iam_client = boto3.client('iam', region_name=AWS_REGION)
lambda_client = boto3.client('lambda', region_name=AWS_REGION)

def create_iam_role():
    """Create IAM Role with basic Lambda execution permissions."""
    try:
        # Check if role already exists
        role = iam_client.get_role(RoleName=ROLE_NAME)
        print(f"Role {ROLE_NAME} already exists.")
        return role['Role']['Arn']
    except iam_client.exceptions.NoSuchEntityException:
        pass

    # Create the role
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        ]
    }
    role = iam_client.create_role(
        RoleName=ROLE_NAME,
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )
    print(f"Created IAM Role: {ROLE_NAME}")

    # Attach basic Lambda execution policy
    iam_client.attach_role_policy(
        RoleName=ROLE_NAME,
        PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    )
    print(f"Attached AWSLambdaBasicExecutionRole to {ROLE_NAME}")

    return role['Role']['Arn']