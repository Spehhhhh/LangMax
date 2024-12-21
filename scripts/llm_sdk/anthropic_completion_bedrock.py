import asyncio
import os

from anthropic import AnthropicBedrock, AsyncAnthropicBedrock
from rich import print

sync_client = AnthropicBedrock(
    aws_access_key=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)
async_client = AsyncAnthropicBedrock(
    aws_access_key=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)


def sync_completion():
    message = sync_client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello!",
            }
        ],
        model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    )
    return message


async def async_completion():
    message = await async_client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello!",
            }
        ],
        model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    )
    return message


if __name__ == "__main__":
    print(sync_completion())
    print(asyncio.run(async_completion()))
