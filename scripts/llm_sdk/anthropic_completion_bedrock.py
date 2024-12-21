import os
from rich import print
from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    aws_access_key=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello!",
        }
    ],
    model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
)

print(message)
