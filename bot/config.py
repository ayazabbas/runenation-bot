import boto3
import botocore
import os
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv("ENV")
S3_BUCKET = os.getenv("S3_BUCKET")
GOOGLE_SECRET_S3_KEY = os.getenv("GOOGLE_SECRET_S3_KEY")
TOKEN = os.getenv("DISCORD_TOKEN")

# download client_secret.json for authenticating with Google API
s3 = boto3.client("s3")
s3.download_file(S3_BUCKET, GOOGLE_SECRET_S3_KEY, "client_secret.json")
