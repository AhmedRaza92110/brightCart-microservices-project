from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
class OrderRequest(BaseModel):
    user_id: str = "demo-user"
    items: list[dict] = Field(default_factory=list)
    total: float = 0


app = FastAPI(title="Orders Service", version="1.0.0")
ORDERS = [{"id":"BC-1042","items":2,"total":131.00,"status":"delivered"},{"id":"BC-1041","items":1,"total":42.00,"status":"processing"}]

@app.get("/health")
def health():
    return {"status": "ok", "service": "order-service"}

@app.get("/orders")
def get_orders():
    """List demo orders."""
    return ORDERS

@app.post("/orders")
def endpoint(payload: OrderRequest):
    """Create a demo order."""
    order = {"id": f"BC-{1000 + len(ORDERS)}", **payload.model_dump(), "status": "created"}
    ORDERS.append(order)
    return order

