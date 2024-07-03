from fastapi import FastAPI

app = FastAPI()

# uvicorn main:app --reload
@app.get("/")
async def root():
    return {"message": "Hello World"}