from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from src.api import auth
from src import database as db
import sqlalchemy

router = APIRouter(
    prefix="/stats",
    tags=["stats"],
    dependencies=[Depends(auth.get_api_key)],
)


class Input(BaseModel):
    income: int
    state: str
    weight: int #lbs
    height: int #in

# uvicorn src.api.server:app --host 0.0.0.0 --port 3001

@router.get("/")
async def root():
    return {"message": "Testing"}