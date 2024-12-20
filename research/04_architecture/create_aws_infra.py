from aws_roles import create_update_role
from aws_lambda import create_update_lambda


if __name__ == "__main__":
    # Step 1: Create IAM role
    role_arn = create_update_role()

    # Step 2: Deploy Lambda function
    create_update_lambda(role_arn)