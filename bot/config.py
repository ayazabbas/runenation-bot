import boto3
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv("ENV")
S3_BUCKET = os.getenv("CONFIG_S3_BUCKET")
GOOGLE_SECRET_S3_KEY = os.getenv("GOOGLE_SECRET_S3_KEY")
TOKEN = os.getenv("DISCORD_TOKEN")

# download client_secret.json for authenticating with Google API
s3 = boto3.client('s3')
with open('client_secret.json', 'wb') as f:
    s3.download_fileobj(S3_BUCKET, GOOGLE_SECRET_S3_KEY, f)
