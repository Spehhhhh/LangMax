import anthropic
from pool_private import anthropic_edu_pool_002

client = anthropic.Anthropic(
    api_key=anthropic_edu_pool_002,
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[{"role": "user", "content": "How are you today?"}],
)

print(message.content)

import anthropic

anthropic.Anthropic().messages.create(
    model="claude-2.1",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, world"}],
)
