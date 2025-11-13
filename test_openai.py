import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # lee .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello from my Windows desktop setup!"}],
)
print(resp.choices[0].message.content)
print("Tokens:", resp.usage.total_tokens if hasattr(resp, "usage") else "n/a")
