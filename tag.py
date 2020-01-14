import boto3

lambda_client = boto3.client('lambda', region_name='us-east-2')
initial_lambda = []
final_lambdas = []

#Creating Paginator for Lambda
paginator = lambda_client.get_paginator('list_functions')
page_iterator = paginator.paginate()

#For loop for filtering only functionsarns of all the functions
for page in page_iterator:
    initial_lambda += [function['FunctionArn'] for function in page['Functions']]

#For loop for filtering out only those lambdas with prefix name connect-prod
for name in initial_lambda:
    if 'prod' in name:
        final_lambdas.append(name)

#tagging all the filtered out lambdas
for name in final_lambdas:
    response = lambda_client.tag_resource(
        Resource=name,
        Tags={
            'ENV': 'PROD'
        }
    )

#print(final_lambdas)

