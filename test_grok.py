from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

response = client.chat.completions.create(
    model="grok-4-1-fast-reasoning",
    messages=[
        {
            "role": "user",
            "content": "Say hello from Grok API"
        }
    ]
)

print(response.choices[0].message.content)