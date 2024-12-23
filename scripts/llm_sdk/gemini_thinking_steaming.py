import asyncio

from google import genai

client = genai.Client()

for chunk in client.models.generate_content_stream(
    model="gemini-2.0-flash-thinking-exp",
    contents="游戏王有什么禁卡？",
):
    for part in chunk.candidates[0].content.parts:  # type: ignore
        if part.thought:
            print(f"Model Thought Chunk:\n{part.text}\n")
        else:
            print(f"\nModel Response:\n{part.text}\n")


async def main():
    chat = client.aio.chats.create(model="gemini-2.0-flash-thinking-exp")
    response = await chat.send_message("游戏王有什么禁卡？")
    print(response.text)
    response = await chat.send_message("你在想什么？")
    print(response.text)


asyncio.run(main())
