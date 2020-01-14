import boto3

final_url = []
sqs_client = boto3.client('sqs', region_name='us-east-2')
s3_client = boto3.client('s3')
response = sqs_client.list_queues(
    QueueNamePrefix='prod'
)
for url in response['QueueUrls']:
    final_url.append(url)

for sqs_url in final_url:
    response = sqs_client.tag_queue(
        QueueUrl=sqs_url,
        Tags={
            'ENV': 'PROD'
        }
    )