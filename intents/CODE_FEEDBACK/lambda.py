import json
import boto3
import secrets
import datetime

def lambda_handler(event, context):
    client = boto3.client('codeguru-reviewer')
    repository = event['currentIntent']['slotDetails']['repository']['resolutions'][0]['value']
    branch_name = event['currentIntent']['slotDetails']['branch']['resolutions'][0]['value']
    
    response = client.list_code_reviews(
        Type='RepositoryAnalysis',
        RepositoryNames=[repository],
        ProviderTypes=['GitHub'],
        States=['Completed'])
    unsorted_code_reviews = response['CodeReviewSummaries']
    
    code_review = sorted(unsorted_code_reviews, key=lambda c: c['CreatedTimeStamp'], reverse=True)[0]
    code_review_arn = code_review['CodeReviewArn']
    
    recommendations = client.list_recommendations(CodeReviewArn=code_review_arn)['RecommendationSummaries']
    recommendations_text = ''
    for recommendation in recommendations:
        recommendations_text += recommendation['Description']
        recommendations_text += '\n'
    
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "Your recommendations are: \n"+ recommendations_text
            }
        }
    }
    
    return response

