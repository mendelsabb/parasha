# services/openai_service.py
from openai import AsyncOpenAI
from fastapi import Depends
from functools import lru_cache
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class OpenAIService:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def generate_discourse(self, parasha_name: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable rabbi providing insights on Torah portions."},
                {"role": "user", "content": f"Generate a brief biblical discourse and exegesis about the Torah portion {parasha_name}."}
            ]
        )
        return response.choices[0].message.content

@lru_cache()
def get_openai_service():
    return OpenAIService()