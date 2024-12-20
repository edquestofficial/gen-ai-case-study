from aws_s3.create_bucket import create_s3_bucket
from aws_roles.create_update_role import create_iam_role
from aws_lambda.create_update_lambda import  create_or_update_lambda_function

bucket_name = "my-edquest-bucket-name-1" 
print(f"bucket_name --- ", bucket_name)
# Step 1: Create IAM role
create_s3_bucket(bucket_name)

role_arn = create_iam_role()

# Step 2: Deploy Lambda function
create_or_update_lambda_function(role_arn)

# if __name__ == "__main__":
#     # Step 1: Create IAM role
#     create_bucket_new1.create_s3_bucket("gen-ai-poc-73033558046723", "us-east-1")
#     role_arn = create_update_role.create_iam_role()

#     # Step 2: Deploy Lambda function
#     create_update_lambda.create_or_update_lambda_function(role_arn)