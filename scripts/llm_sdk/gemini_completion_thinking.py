import os

from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash-thinking-exp-1219",
    contents="Why 1 + 1 = 2",
)
print(response.model_dump_json())
