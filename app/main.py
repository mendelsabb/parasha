from fastapi import FastAPI
from app.routes import parasha
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.include_router(parasha.router)