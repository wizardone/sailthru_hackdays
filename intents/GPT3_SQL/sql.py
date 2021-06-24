import os
import openai
import json

# Load your API key from an environment variable or secret management service


def lambda_handler(event, context):

    openai.api_key = os.getenv("OPENAI_API_KEY")
    sql_to_convert = event['currentIntent']['slotDetails']['sql']['originalValue']

    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Create a SQL request to {sql_to_convert}:\n\nSELECT",
        temperature=0.3,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    
    ok_response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": f"SELECT {response['choices'][0]['text']}"
            }
        }
    }
    
    return ok_response

if __name__ == "__main__":
    lambda_handler("","")