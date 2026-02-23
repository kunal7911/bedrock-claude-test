#!/usr/bin/env python3
"""
Test script for AWS Bedrock with Claude models
Tests the configured zylum user and model setup
"""

import boto3
import json
import os
from datetime import datetime

def test_bedrock_claude():
    """Test Bedrock API with a simple question about planets"""

    # Create output file with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"bedrock_test_output_{timestamp}.txt"

    def log_and_print(message):
        """Helper function to print and write to file"""
        print(message)
        with open(output_file, 'a') as f:
            f.write(message + '\n')

    # Get region from environment or use default
    region = os.environ.get('AWS_REGION', 'us-east-1')

    # Initialize Bedrock runtime client
    bedrock_runtime = boto3.client(
        service_name='bedrock-runtime',
        region_name=region
    )

    # Get the model ID from environment or use default inference profile
    model_id = os.environ.get('ANTHROPIC_DEFAULT_SONNET_MODEL', 'us.anthropic.claude-sonnet-4-6')

    log_and_print(f"Testing Bedrock with model: {model_id}")
    log_and_print(f"Region: {region}")
    log_and_print("-" * 60)

    # Prepare the request
    prompt = "How many planets are there in the solar system?"

    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        # Make the API call
        log_and_print(f"Question: {prompt}\n")

        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )

        # Parse the response
        response_body = json.loads(response['body'].read())
        answer = response_body['content'][0]['text']

        log_and_print(f"Answer: {answer}\n")
        log_and_print("-" * 60)
        log_and_print("✓ Bedrock test successful!")
        log_and_print(f"✓ User authentication working")
        log_and_print(f"✓ Model {model_id} accessible")
        log_and_print("-" * 60)
        log_and_print(f"Output saved to: {output_file}")

        return True

    except Exception as e:
        log_and_print(f"✗ Error testing Bedrock: {str(e)}")
        return False

if __name__ == "__main__":
    test_bedrock_claude()
