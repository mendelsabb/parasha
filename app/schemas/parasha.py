# schemas/parasha.py
from pydantic import BaseModel

class ParashaRequest(BaseModel):
    parasha_name: str

class ParashaResponse(BaseModel):
    parasha_name: str
    discourse: str