# aws_s3_demo.py
# Demo: Uploading and downloading files from AWS S3 using boto3

import boto3
from botocore.exceptions import NoCredentialsError

# Configure your AWS credentials in ~/.aws/credentials or use environment variables
# Example bucket name (change to your own)
BUCKET_NAME = "my-demo-s3-bucket-12345"
FILE_TO_UPLOAD = "demo.txt"

# Initialize S3 client
s3 = boto3.client('s3')

def upload_file(file_name, bucket, object_name=None):
    try:
        if object_name is None:
            object_name = file_name
        s3.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to bucket {bucket} as {object_name}.")
    except FileNotFoundError:
        print("File not found.")
    except NoCredentialsError:
        print("AWS credentials not available.")

def download_file(bucket, object_name, file_name=None):
    try:
        if file_name is None:
            file_name = object_name
        s3.download_file(bucket, object_name, file_name)
        print(f"File {object_name} downloaded from bucket {bucket} as {file_name}.")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    # Upload a file
    upload_file(FILE_TO_UPLOAD, BUCKET_NAME)
    
    # Download the file back
    download_file(BUCKET_NAME, FILE_TO_UPLOAD, "downloaded_demo.txt")
