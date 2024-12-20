from aws_s3 import create_bucket
from aws_roles import create_update_role
from aws_lambda import  create_update_lambda

if __name__ == "__main__":
    # Step 1: Create IAM role
    # create_bucket_new1.create_s3_bucket("gen-ai-poc-73033558046723", "us-east-1")
    # bucket_name = "my-edquest-bucket-name-111"
    # region = "us-east-1"
    print(f"bucket name -- ", bucket_name)
    create_bucket.create_s3_bucket("my-edquest-bucket-name-1111", "us-east-1")
    role_arn = create_update_role.create_iam_role()

    # Step 2: Deploy Lambda function
    create_update_lambda.create_or_update_lambda_function(role_arn)