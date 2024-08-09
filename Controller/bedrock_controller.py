# CONTROLLER MODULE FOR BEDROCK CLIENT

import json
from botocore.exceptions import ClientError
from Helpers.config import create_client

# BEDROCK CLIENT CREATION
bedrock_client = create_client('bedrock-runtime', 'us-east-1')

# BEDROCK MODEL ID
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

# INVOKE BEDROCK MODEL
def invoke_bedrock_model(prompt):
    native_request = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.5,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    }

    request = json.dumps(native_request)

    try:
        response = bedrock_client.invoke_model(modelId=model_id, body=request)
        model_response = json.loads(response["body"].read())
        return model_response["content"][0]["text"]
    except (ClientError, Exception) as e:
        return f"ERROR: Can't invoke '{model_id}'. Reason: {e}"
