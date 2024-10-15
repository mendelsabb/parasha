from fastapi import FastAPI
from app.routes import parasha
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the FastAPI app with a custom title for the Swagger UI
app = FastAPI(title="Parasha")

app.include_router(parasha.router)
