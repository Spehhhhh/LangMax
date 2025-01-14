import litellm

litellm.callbacks = ["logfire"]

response = litellm.completion(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you?",
        },
    ],
)