from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI(title="Product Catalog Service", version="1.0.0")
PRODUCTS = [
 {"id":"p1","name":"Cloud Runner Sneakers","category":"Footwear","price":89.00,"color":"#dff7ee","emoji":"👟","badge":"BESTSELLER"},
 {"id":"p2","name":"Everyday Tote","category":"Accessories","price":42.00,"color":"#fff0d9","emoji":"👜","badge":"NEW"},
 {"id":"p3","name":"Studio Headphones","category":"Electronics","price":129.00,"color":"#eee7ff","emoji":"🎧","badge":"TOP RATED"},
 {"id":"p4","name":"Ceramic Travel Mug","category":"Lifestyle","price":28.00,"color":"#ffe6e9","emoji":"☕","badge":"ECO PICK"},
 {"id":"p5","name":"Weekend Camera","category":"Electronics","price":219.00,"color":"#e4f0ff","emoji":"📷","badge":"LIMITED"},
 {"id":"p6","name":"Soft Knit Hoodie","category":"Apparel","price":74.00,"color":"#f4e8ff","emoji":"🧥","badge":"TRENDING"}
]

@app.get("/health")
def health():
    return {"status": "ok", "service": "product-service"}

@app.get("/products")
def get_products():
    """List catalog products."""
    return PRODUCTS

@app.get("/products/{product_id}")
def get_products_product_id(product_id: str):
    """Get product by ID."""
    return next((p for p in PRODUCTS if p["id"] == product_id), {"error": "not found"})

