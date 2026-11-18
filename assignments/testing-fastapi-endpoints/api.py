from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Test API")


class EchoMessage(BaseModel):
    message: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/echo", response_model=EchoMessage)
def echo_message(payload: EchoMessage):
    return payload