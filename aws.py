import boto3

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name="us-east-1"
)

# Send your sms message.
client.publish(
    PhoneNumber="+",
    Message="Hello World!"
)