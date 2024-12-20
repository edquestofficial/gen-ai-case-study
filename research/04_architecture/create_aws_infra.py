from aws_s3 import create_bucket_new
from aws_roles import create_update_role
from aws_lambda import create_update_lambda


if __name__ == "__main__":
    # Step 1: Create IAM role
    create_bucket_new.create_s3_bucket("my-unique-bucket-name-12345", "us-east-1")
    role_arn = create_update_role.create_iam_role()

    # Step 2: Deploy Lambda function
    create_update_lambda.create_or_update_lambda_function(role_arn)