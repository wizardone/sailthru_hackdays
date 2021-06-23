import json
import boto3
import secrets

def lambda_handler(event, context):
    client = boto3.client('codeguru-reviewer')
    repository = event['currentIntent']['slotDetails']['repository']['resolutions'][0]['value']
    branch_name = event['currentIntent']['slotDetails']['branch']['resolutions'][0]['value']
    
    response = client.create_code_review(
        Name=repository + '-'+ branch_name + '-' + secrets.token_hex(16),
        RepositoryAssociationArn="arn:aws:codeguru-reviewer:us-east-1:892579079126:association:eb328a26-5f01-4cf6-89ee-11f7567ed397",
        Type={
            'RepositoryAnalysis': {
                'RepositoryHead': {
                    'BranchName': branch_name
                }
            }
        }
    )
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Ok')
    }

