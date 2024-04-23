import openai

openai.api_key = ""
openai.api_base = "https://openai.ehco-relay.cc/"

response = openai.ChatCompletion.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "1_1?"},
    ],
)

print(response["choices"][0]["message"]["content"])
