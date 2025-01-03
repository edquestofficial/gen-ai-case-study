from aws_s3 import create_bucket
from aws_s3 import create_edquest_bucket
from aws_roles import create_update_role
from aws_lambda import  create_update_lambda, edquest_create_update_lambda
from config.config import IAM_ROLES, CONFIG

if __name__ == "__main__":
    # Step 1: Create IAM role
    # bucket_name = "post-call-analysis-1234"
    # region = "us-east-1"
    # create_bucket.create_s3_bucket(bucket_name, region)

    # For bucket creation
    # s3_config = CONFIG["Audio_To_Transcript"]["s3"]
    # create_edquest_bucket.create_s3_bucket(s3_config)
    
    # create_bucket.create_s3_bucket("post-call-analysis-1234", "us-east-1")

    # Create IAM ROLE
    Audio_To_Transcript_Role = IAM_ROLES["Audio_To_Transcript_Role"]
    print("Audio_To_Transcript_Role ---- ", Audio_To_Transcript_Role)

    audio_to_transcript_role_arn = create_update_role.create_iam_role(Audio_To_Transcript_Role)

    print(f"audio_to_transcript_role_arn : {audio_to_transcript_role_arn}")
    
    # # Step 2: Deploy Lambda function
    edquest_create_update_lambda.create_or_update_lambda_function(audio_to_transcript_role_arn)
    # create_update_lambda.create_or_update_lambda_function(audio_to_transcript_role_arn)

    # # 
    # # TRANSCRIPT_TO_ANALYSIS_ROLE = IAM_ROLES["TRANSCRIPT_TO_ANALYSIS_ROLE"]
    # # transcript_to_analysis_role_arn = create_update_role.create_iam_role(TRANSCRIPT_TO_ANALYSIS_ROLE)

    # # Step 2: Deploy Lambda function
    # # create_update_lambda.create_or_update_lambda_function(transcript_to_analysis_role_arn)



    #   # Create IAM ROLE for text summarization
    # Text_To_Summarization_Role = IAM_ROLES["Text_To_Summarization_Role"]
    # print("Text_To_Summarization_Role ---- ", Text_To_Summarization_Role)

    # text_to_summarization_Role_arn = create_update_role.create_iam_role(Text_To_Summarization_Role)

    # print(f"Text_To_Summarization_Role_arn : {text_to_summarization_Role_arn}")