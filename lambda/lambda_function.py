import os
import boto3
import json

ENDPOINT_NAME = os.environ["ENDPOINT_NAME"]

runtime = boto3.client("runtime.sagemaker")


def lambda_handler(event, context):
    data = event.replace("\n", "").replace(" ", "")

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME, ContentType="text/csv", Body=data
    )

    result = json.loads(response['Body'].read().decode())
    pred = int(round(result, 0))
    prob = round(result, 2)
    
  return {
    'statusCode': 200,
    'prediction': json.dumps(pred),
    'probabilty': json.dumps(prob)
    }
