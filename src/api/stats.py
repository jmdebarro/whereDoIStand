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
    gender: str
    weight: int #lbs
    height: int #in

# uvicorn src.api.server:app --host 0.0.0.0 --port 3001

@router.post("/")
async def postStats(stats: Input):

    # Formatting input
    state = stats.state.lower().capitalize()
    gender = stats.gender.lower().capitalize()
    state_gender = state + "_" + gender
    state += "_Total"
   
    national_col = '"medianIncome"'
    state_col = f'"{state}"'
    gender_col = f'"{state_gender}"'

    sql = f"""
        SELECT {national_col} AS medianIncome, {state_col} AS state_median, {gender_col} AS gender_median
        FROM median
    """
    
    with db.engine.begin() as connection:
        result = connection.execute(sqlalchemy.text(sql)).fetchone()
        print(result)
        nationalMedian = result[0]
        stateMedian = result[1]
        genderMedian = result[2]

        response = {"national" : stats.income - nationalMedian, 
                    "state": stats.income - stateMedian,
                    "gender": stats.income - genderMedian}

    return response