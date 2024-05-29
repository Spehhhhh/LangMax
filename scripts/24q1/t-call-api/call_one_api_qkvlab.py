from openai import OpenAI

YOUR_KEY = "sk-ui5YzB96L65r0O9yEeC71b271b20499a92D34eC4EcF54cB3"
YOUR_BASE_URL = "https://one-api.qkvlab.com/v1"
YOUR_MODEL = "claude-3-opus-20240229"

client = OpenAI(api_key=YOUR_KEY)
client.base_url = YOUR_BASE_URL

completion = client.chat.completions.create(
    model=YOUR_MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
)

print(completion.choices[0].message)
