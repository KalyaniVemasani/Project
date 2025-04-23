import boto3
import json


lambda_client = boto3.client('lambda', region_name='us-east-1')  # Change region if needed


function_name = 'myprojects3function'
payload = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "myprojects3bucket698"
                },
                "object": {
                    "key": "example1.txt"
                }
            }
        }
    ]
}

# Invoke the Lambda function
response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',
    Payload=json.dumps(payload)
)


response_payload = response['Payload'].read().decode('utf-8')
print(" Lambda Response:")
print(response_payload)
