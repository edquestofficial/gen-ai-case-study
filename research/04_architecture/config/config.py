IAM_ROLES = {
  "Audio_To_Transcript_Role": {
    "role_name": "Audio_To_Transcript_Role",
    "trust_policy": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": [
                  "logs:PutLogEvents",
                  "logs:CreateLogGroup",
                  "logs:CreateLogStream"
                ],
                "Resource": "arn:aws:logs:*:*:*"
            },
            {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": ["s3:GetObject", "s3:PutObject"],
                "Resource": "arn:aws:s3:::*/*"
            },
        ]
    }
  },
  "TRANSCRIPT_TO_ANALYSIS_ROLE": {
    "role_name": "TRANSCRIPT_TO_ANALYSIS_ROLE",
    "trust_policy": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": ["s3:getObject",
                           "s3:putObject",
                           "bedrock"],
            }
        ]
    }
  },
}



BUCKET_NAME = "edquest-post-call-analysis"
REGIN_NAME = "us-east-1"
CONFIG= {
    "Audio_To_Transcript" : {
        "s3" : {
            "bucket_name" : BUCKET_NAME,
            "directory_list" : ["audio", "audio_processed", "transcript"],
            "region" : REGIN_NAME,
        },
        "lambda": {
            "REGION_NAME" : REGIN_NAME,
            "LAMBDA_FUNCTION_NAME" : "test_lambda",
            "ROLE_NAME" : "LambdaExecutionRole",
            "POLICY_NAME" : "LambdaBasicPolicy",
            "LAMBDA_CODE_DIR" : "/functions",
            "ZIP_FILE_NAME" : "post_call_analysis.zip",
            "S3_EVENT" : "s3:ObjectCreated:*",
            "BUCKET_NAME" : BUCKET_NAME,
            'LambdaFunctionConfigurations': [
                {
                    # regino = us-east-1, account_id = AWS_ACCOUNT_ID, event_name = test_lambda
                    'LambdaFunctionArn': "arn:aws:lambda:us-east-1:AWS_ACCOUNT_ID:function:test_lambda", 
                    'Events': ["s3:ObjectCreated:*"],  # Specify the event you want to trigger the Lambda function
                    "Filter": {
                        "Key": {
                            "FilterRules": [
                                {"Name": "prefix", "Value": "audio/"},
                                {"Name": "suffix", "Value": "dialog.mp3"},
                            ]
                        }
                    }
                },
            ],
        },
        "iam_role": {
            "Audio_To_Transcript_Role": {
                "role_name": "Audio_To_Transcript_Role",
                "trust_policy": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {"Service": "lambda.amazonaws.com"},
                            "Action": [
                            "logs:PutLogEvents",
                            "logs:CreateLogGroup",
                            "logs:CreateLogStream"
                            ],
                            "Resource": "arn:aws:logs:*:*:*"
                        },
                        {
                            "Effect": "Allow",
                            "Principal": {"Service": "lambda.amazonaws.com"},
                            "Action": ["s3:GetObject", "s3:PutObject"],
                            "Resource": "arn:aws:s3:::*/*"
                        },
                    ]
                }
            },
            "TRANSCRIPT_TO_ANALYSIS_ROLE": {
                "role_name": "TRANSCRIPT_TO_ANALYSIS_ROLE",
                "trust_policy": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {"Service": "lambda.amazonaws.com"},
                            "Action": ["s3:getObject",
                                    "s3:putObject",
                                    "bedrock"],
                        }
                    ]
                }
            },
        },
        "test": lambda name: f"My Name is {name}"
    }
}
