import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)
print(message.content)
