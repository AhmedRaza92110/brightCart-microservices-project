from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
class PaymentRequest(BaseModel):
    order_id: str
    amount: float = Field(gt=0)
    currency: str = "USD"


app = FastAPI(title="Payments Service", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "payment-service"}

@app.post("/payments")
def endpoint(payload: PaymentRequest):
    """Create a mock payment (no real charge)."""
    return {"payment_id": "pay_demo_001", "order_id": payload.order_id, "amount": payload.amount, "currency": payload.currency, "status": "authorized_demo"}

