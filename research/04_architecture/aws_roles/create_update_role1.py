import boto3
import json

AWS_REGION = "us-east-1"
ROLE_NAME = "LambdaExecutionRole1"
POLICY_NAME = "LambdaBasicPolicy"

# Initialize AWS clients
iam_client = boto3.client('iam', region_name=AWS_REGION)
lambda_client = boto3.client('lambda', region_name=AWS_REGION)

def create_iam_role(role_config):
    role_name = role_config["role_name"]
    trust_policy = role_config["trust_policy"]
    print("role_name ---- ", role_name)
    print("trust_policy ---- ", trust_policy)
    print("trust_policy ---- ", type(trust_policy))

    """Create IAM Role with basic Lambda execution permissions."""
    try:
        # Check if role already exists
        role = iam_client.get_role(RoleName=role_name)
        print(f"Role {role_name} already exists.")
        return role['Role']['Arn']
    except iam_client.exceptions.NoSuchEntityException:
        pass

    # Define the trust policy for Lambda execution
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"  # Lambda service can assume this role
            }
        ]
    }

    # Define the permission policy
    permission_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "logs:PutLogEvents",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream"
                ],
                "Resource": "arn:aws:logs:*:*:*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject"
                ],
                "Resource": [
                    # "arn:aws:s3:::my-edquest-bucket-name-1111",
                    # "arn:aws:s3:::my-edquest-bucket-name-1111/",
                    "arn:aws:s3:::my-edquest-bucket-name-1111/audio/*",
                    "arn:aws:s3:::my-edquest-bucket-name-1111/audio-to-text/*"
                ]
            },
            # {
            #     "Effect": "Allow",
            #     "Action": [
            #         "s3:GetObject",
            #         "s3:PutObject"
            #     ],
            #     "Resource": [
            #         "arn:aws:s3:::my-edquest-bucket-name-1111",
            #         "arn:aws:s3:::my-edquest-bucket-name-1111/",
            #         "arn:aws:s3:::my-edquest-bucket-name-1111/audio-to-text/*"
            #     ]
            # },
            {
                "Effect": "Allow",
                "Action": "cloudwatch:PutMetricData",
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": ["transcribe:StartTranscriptionJob",
                            "transcribe:GetTranscriptionJob",
                            "transcribe:ListTranscriptionJobs",
                            "transcribe:DeleteTranscriptionJob"
                        ],
                "Resource": "arn:aws:transcribe:us-east-1:730335580467:*"
            }
        ]
    }

    # Create the role with the trust policy
    role = iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )
    print(f"Created IAM Role: {role_name}")

    # Attach the permission policy to the role
    iam_client.put_role_policy(
        RoleName=role_name,
        PolicyName="LambdaPermissionsPolicy",  # Policy name
        PolicyDocument=json.dumps(permission_policy)
    )
    print(f"Attached permission policy to {role_name}")

    # Attach the AWSLambdaBasicExecutionRole policy
    iam_client.attach_role_policy(
        RoleName=role_name,
        PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    )
    print(f"Attached AWSLambdaBasicExecutionRole to {role_name}")

    return role['Role']['Arn']
