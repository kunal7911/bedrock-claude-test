# AWS Bedrock Claude Test

Test script for AWS Bedrock integration with Claude models.

## Setup

This project tests the AWS Bedrock configuration with Claude Sonnet 4.6 model.

### Prerequisites

- Python 3.9+
- boto3 library
- AWS credentials configured
- Access to AWS Bedrock

### Installation

```bash
pip3 install boto3
```

### Environment Variables

Required environment variables:
- `AWS_REGION` - AWS region (default: us-east-1)
- `ANTHROPIC_DEFAULT_SONNET_MODEL` - Model ID for Claude Sonnet
- `AWS_BEARER_TOKEN_BEDROCK` - Bedrock authentication token

### Usage

Run the test script:

```bash
python3 test_bedrock.py
```

### Test Results

The script tests a simple question: "How many planets are there in the solar system?"

Expected output:
- ✓ Bedrock test successful
- ✓ User authentication working
- ✓ Model accessible

## Date

Created: 2026-02-23
