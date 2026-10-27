from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class HealthCheck(BaseModel):
    status: str


@app.get("/health", response_model=HealthCheck)
async def health_check():
    return HealthCheck(status="ok")
