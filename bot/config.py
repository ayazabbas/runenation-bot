import boto3
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv("ENV")
S3_BUCKET = os.getenv("CONFIG_S3_BUCKET")
GOOGLE_SECRET_S3_KEY = os.getenv("GOOGLE_SECRET_S3_KEY")
if ENV == "dev":
    TOKEN = os.getenv("DISCORD_TOKEN_DEV")
else:
    TOKEN = os.getenv("DISCORD_TOKEN")

# download client_secret.json for authenticating with Google API