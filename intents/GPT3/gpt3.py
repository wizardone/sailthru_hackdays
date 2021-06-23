import os
import openai

# Load your API key from an environment variable or secret management service


def lambda_handler(event, context):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
