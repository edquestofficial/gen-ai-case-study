from aws_s3 import create_bucket
from aws_roles import create_update_role1
from aws_lambda import  create_update_lambda
from config.config import IAM_ROLES

if __name__ == "__main__":
    # Step 1: Create IAM role
    bucket_name = "my-edquest-bucket-name-1111"
    region = "us-east-1"
    # create_bucket.create_s3_bucket(bucket_name, region)
    create_bucket.create_s3_bucket("my-edquest-bucket-name-1111", "us-east-1")

    # Create IAM ROLE
    Audio_To_Transcript_Role = IAM_ROLES["Audio_To_Transcript_Role"]
    print("Audio_To_Transcript_Role ---- ", Audio_To_Transcript_Role)

    audio_to_transcript_role_arn = create_update_role1.create_iam_role(Audio_To_Transcript_Role)
    
    # Step 2: Deploy Lambda function
    create_update_lambda.create_or_update_lambda_function(audio_to_transcript_role_arn)

    # 
    # TRANSCRIPT_TO_ANALYSIS_ROLE = IAM_ROLES["TRANSCRIPT_TO_ANALYSIS_ROLE"]
    # transcript_to_analysis_role_arn = create_update_role.create_iam_role(TRANSCRIPT_TO_ANALYSIS_ROLE)

    # Step 2: Deploy Lambda function
    # create_update_lambda.create_or_update_lambda_function(transcript_to_analysis_role_arn)