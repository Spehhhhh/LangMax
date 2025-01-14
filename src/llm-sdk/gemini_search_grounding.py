from google import genai
from google.genai.types import GenerateContentConfig, GoogleSearch, Tool

client = genai.Client()
model_id = "gemini-2.0-flash-exp"

google_search_tool = Tool(google_search=GoogleSearch())

response = client.models.generate_content(
    model=model_id,
    contents="游戏王有什么限制卡？",
    config=GenerateContentConfig(
        tools=[google_search_tool],
        response_modalities=["TEXT"],
    ),
)

print(response.candidates[0].model_dump_json(indent=2))  # type: ignore
