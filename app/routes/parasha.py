from fastapi import APIRouter, Depends
from app.schemas.parasha import ParashaRequest, ParashaResponse
from app.services.openai_service import OpenAIService

router = APIRouter()

@router.post("/generate_discourse", response_model=ParashaResponse)
async def generate_discourse(request: ParashaRequest, openai_service: OpenAIService = Depends(OpenAIService)):
    discourse = await openai_service.generate_discourse(request.parasha_name)
    return ParashaResponse(parasha_name=request.parasha_name, discourse=discourse)