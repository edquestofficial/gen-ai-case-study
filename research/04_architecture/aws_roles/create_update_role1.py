# import boto3
# import json
# from botocore.exceptions import ClientError

# AWS_REGION = "us-east-1"
# ROLE_NAME = "LambdaExecutionRole1"
# POLICY_NAME = "LambdaBasicPolicy"

# # Initialize AWS clients
# iam_client = boto3.client('iam', region_name=AWS_REGION)
# lambda_client = boto3.client('lambda', region_name=AWS_REGION)

# def create_iam_role(role_config):
#     role_name = role_config["role_name"]
#     trust_policy = role_config["trust_policy"]
#     print("role_name ---- ", role_name)
#     print("trust_policy ---- ", trust_policy)
#     print("trust_policy ---- ", type(trust_policy))

#     """Create IAM Role with basic Lambda execution permissions."""
#     try:
#         # Check if role already exists
#         role = iam_client.get_role(RoleName=role_name)
#         print(f"Role {role_name} already exists.")
#         # return role['Role']['Arn']
#     except iam_client.exceptions.NoSuchEntityException:
#         pass

#     # Define the trust policy for Lambda execution
#     trust_policy = {
#         "Version": "2012-10-17",
#         "Statement": [
#             {
#                 "Effect": "Allow",
#                 "Principal": {
#                     "Service": "lambda.amazonaws.com"
#                 },
#                 "Action": "sts:AssumeRole"  # Lambda service can assume this role
#             }
#         ]
#     }

#     # Define the permission policy
#     permission_policy = {
#         "Version": "2012-10-17",
#         "Statement": [
#             {
#                 "Effect": "Allow",
#                 "Action": [
#                     "logs:PutLogEvents",
#                     "logs:CreateLogGroup",
#                     "logs:CreateLogStream"
#                 ],
#                 "Resource": "arn:aws:logs:*:*:*"
#             },
#             {
#                 "Effect": "Allow",
#                 "Action": [
#                     "s3:GetObject",
#                     "s3:PutObject"
#                 ],
#                 "Resource": [
#                     "arn:aws:s3:::post-call-analysis-1234",
#                     "arn:aws:s3:::post-call-analysis-1234/",
#                     "arn:aws:s3:::post-call-analysis-1234/audio/*",
#                     "arn:aws:s3:::post-call-analysis-1234/audio-to-text/*"
#                 ]
#             },
#             # {
#             #     "Effect": "Allow",
#             #     "Action": [
#             #         "s3:GetObject",
#             #         "s3:PutObject"
#             #     ],
#             #     "Resource": [
#             #         "arn:aws:s3:::post-call-analysis-1234",
#             #         "arn:aws:s3:::post-call-analysis-1234/",
#             #         "arn:aws:s3:::post-call-analysis-1234/audio-to-text/*"
#             #     ]
#             # },
#             {
#                 "Effect": "Allow",
#                 "Action": "cloudwatch:PutMetricData",
#                 "Resource": "*"
#             },
#             {
#                 "Effect": "Allow",
#                 "Action": ["transcribe:StartTranscriptionJob",
#                             "transcribe:GetTranscriptionJob",
#                             "transcribe:ListTranscriptionJobs",
#                             "transcribe:DeleteTranscriptionJob"
#                         ],
#                 "Resource": "arn:aws:transcribe:us-east-1:730335580467:*"
#             }
#         ]
#     }

#     # # Create the role with the trust policy
#     # role = iam_client.create_role(
#     #     RoleName=role_name,
#     #     AssumeRolePolicyDocument=json.dumps(trust_policy)
#     # )
#     # print(f"Created IAM Role: {role_name}")

#     try:
#         # Try to create the IAM role
#         role = iam_client.create_role(
#             RoleName=role_name,
#             AssumeRolePolicyDocument=json.dumps(trust_policy)
#         )
#         print(f"Created IAM Role: {role_name}")

#     except ClientError as e:
#         if e.response['Error']['Code'] == 'EntityAlreadyExists':
#             print(f"Role {role_name} already exists. Updating the role...")
#         else:
#             print(f"Failed to create role: {e}")
#             raise

#     # Update the trust policy if the role already exists or was just created
#     try:
#         iam_client.update_assume_role_policy(
#             RoleName=role_name,
#             PolicyDocument=json.dumps(trust_policy)
#         )
#         print(f"Updated trust policy for role: {role_name}")
#     except ClientError as e:
#         print(f"Failed to update trust policy: {e}")
#         raise

#     # Attach or update the inline policy
#     try:
#         iam_client.put_role_policy(
#             RoleName=role_name,
#             PolicyName="LambdaPermissionsPolicy",
#             PolicyDocument=json.dumps(permission_policy)
#         )
#         print(f"Attached/Updated permission policy for role: {role_name}")
#     except ClientError as e:
#         print(f"Failed to attach/update permission policy: {e}")
#         raise

#     # Attach AWS managed policy
#     try:
#         iam_client.attach_role_policy(
#             RoleName=role_name,
#             PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
#         )
#         print(f"Attached AWSLambdaBasicExecutionRole policy to {role_name}")
#     except ClientError as e:
#         print(f"Failed to attach AWS managed policy: {e}")
#         raise

#     # # Attach the permission policy to the role
#     # iam_client.put_role_policy(
#     #     RoleName=role_name,
#     #     PolicyName="LambdaPermissionsPolicy",  # Policy name
#     #     PolicyDocument=json.dumps(permission_policy)
#     # )
#     # print(f"Attached permission policy to {role_name}")

#     # # Attach the AWSLambdaBasicExecutionRole policy
#     # iam_client.attach_role_policy(
#     #     RoleName=role_name,
#     #     PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
#     # )
#     # print(f"Attached AWSLambdaBasicExecutionRole to {role_name}")

#     return role['Role']['Arn']
