from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
class MessageRequest(BaseModel):
    channel: str = "email"
    recipient: str
    body: str


app = FastAPI(title="Notifications Service", version="1.0.0")
MESSAGES = [{"id":1,"channel":"email","recipient":"alex@example.com","body":"Your demo order is on its way","status":"sent_demo"}]

@app.get("/health")
def health():
    return {"status": "ok", "service": "message-service"}

@app.post("/messages")
def endpoint(payload: MessageRequest):
    """Queue a demo notification."""
    message = {"id": len(MESSAGES) + 1, **payload.model_dump(), "status": "queued_demo"}
    MESSAGES.append(message)
    return message

@app.get("/messages")
def get_messages():
    """List demo notifications."""
    return MESSAGES

