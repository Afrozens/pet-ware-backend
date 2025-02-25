import boto3
from app.settings import get_settings 

settings = get_settings()

s3 = boto3.client(
    's3',
    aws_access_key_id= settings.BUCKET_KEY,
    aws_secret_access_key = settings.BUCKET_SECRET
)

s3_resource = boto3.resource(
    's3',
    aws_access_key_id= settings.BUCKET_KEY,
    aws_secret_access_key = settings.BUCKET_SECRET
)