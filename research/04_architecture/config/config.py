IAM_ROLES = {
  "AUDIO_TO_TRANSCRIPT_ROLE": {
    "role_name": "AUDIO_TO_TRANSCRIPT_ROLE",
    "trust_policy": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": ["s3:GetObject", "s3:PutObject"],
                # "Resource": "arn:aws:s3:::your-bucket-name/*"
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
                "Action": [],
            }
        ]
    }
  },
}
