from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI(title="Activity History Service", version="1.0.0")
EVENTS = [{"id":1,"event":"Signed in","time":"Today, 9:41 AM"},{"id":2,"event":"Viewed Cloud Runner Sneakers","time":"Today, 9:43 AM"},{"id":3,"event":"Order BC-1042 delivered","time":"Yesterday"}]

@app.get("/health")
def health():
    return {"status": "ok", "service": "history-service"}

@app.get("/history")
def get_history():
    """Get demo activity events."""
    return EVENTS

