# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import json
import urllib.parse
import boto3
import uuid

print('Loading function')

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    destination_bucket = source_bucket  # Default to the same bucket
    destination_key = source_key.replace("audio/", "audio-to-text/")
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        print("#########################################")
        print(f"event details : {event['Records'][0]}")

        copy_source = {'Bucket': source_bucket, 'Key': source_key}
        s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=destination_key)
        print("#########################################")
        print(f"File copied from {source_key} to {destination_key}")
        # transcribe_client = boto3.client('transcribe', region_name='us-east-1')
        # job_name = 'transcription-job-' + str(uuid.uuid4())
        # audio_file_uri = f's3://post-call-analysis-1234/audio/dialog.mp3'

        # response = transcribe_client.start_transcription_job(
        #     TranscriptionJobName=job_name,
        #     Media={'MediaFileUri': audio_file_uri},
        #     MediaFormat='mp3',
        #     LanguageCode='en-US',
        #     OutputBucketName="post-call-analysis-1234",
        #     # OutputKey="audio-to-text/",
        #     Settings={
        #         'ShowSpeakerLabels': True,
        #         'MaxSpeakerLabels': 2
        #     }
        # )
        print(f"CONTENT TYPE:  {response}")
        # return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
              
