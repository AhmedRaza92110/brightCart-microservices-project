from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
class LoginRequest(BaseModel):
    email: str
    password: str


app = FastAPI(title="Authentication Service", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "auth-service"}

@app.post("/login")
def endpoint(payload: LoginRequest):
    """Demo login endpoint."""
    return {"access_token": "demo-token", "token_type": "bearer", "user": {"id": 1, "email": payload.email}}

