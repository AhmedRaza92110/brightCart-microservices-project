from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI(title="Profile Service", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "profile-service"}

@app.get("/profiles/{user_id}")
def get_profiles_user_id(user_id: str):
    """Get a sample profile."""
    return {"id": user_id, "name": "Alex Morgan", "email": "alex@example.com", "tier": "Bright+"}

