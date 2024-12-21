terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.66.0"
    }
  }
}

provider "aws" {
    region = var.region
}

# Data source to get AWS account ID
data "aws_caller_identity" "current" {}

# Create S3 bucket with a name using a hardcoded string and account number
resource "aws_s3_bucket" "dev_genai_bucket" {
  bucket = "dev-genai-${data.aws_caller_identity.current.account_id}"
  acl    = "private"

  tags = {
    Name        = "S3 Bucket"
    Environment = "Dev"
  }
}

# # Set the bucket ACL using aws_s3_bucket_acl
# resource "aws_s3_bucket_acl" "dev_genai_bucket_acl" {
#   bucket = aws_s3_bucket.dev_genai_bucket.id
#   acl    = "private"
# }

# Create three directories inside the S3 bucket
resource "aws_s3_object" "audio" {
  bucket = aws_s3_bucket.dev_genai_bucket.id
  key    = "audio/"
  etag   = "d41d8cd98f00b204e9800998ecf8427e" # Empty directory placeholder
}

resource "aws_s3_object" "audio_to_text" {
  bucket = aws_s3_bucket.dev_genai_bucket.id
  key    = "audio_to_text/"
  etag   = "d41d8cd98f00b204e9800998ecf8427e"
}

resource "aws_s3_object" "output_summary" {
  bucket = aws_s3_bucket.dev_genai_bucket.id
  key    = "output_summary/"
  etag   = "d41d8cd98f00b204e9800998ecf8427e"
}

# Outputs to verify resource creation
output "bucket_name" {
  value = aws_s3_bucket.dev_genai_bucket.bucket
}

output "directories" {
  value = [
    aws_s3_object.audio.key,
    aws_s3_object.audio_to_text.key,
    aws_s3_object.output_summary.key
  ]
}
