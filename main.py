from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
import uuid

app = FastAPI()

# Establish connection to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["ecommerce"]  # database name

# Define MongoDB collections
products_collection = db["products"]
orders_collection = db["orders"]


class Product(BaseModel):
    name: str
    price: float
    quantity: int


class Item(BaseModel):
    product_id: int
    bought_quantity: int


class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str


class Order(BaseModel):
    id: str = str(uuid.uuid4())
    timestamp: str
    items: List[Item]
    total_amount: float = None
    user_address: UserAddress


@app.get("/products")
async def list_products():
    products = products_collection.find({})
    return [product for product in products]


@app.post("/products")
async def create_product(product: Product):
    product_data = product.dict()
    product_data["_id"] = str(uuid.uuid4())
    products_collection.insert_one(product_data)
    return product_data


@app.post("/orders")
def create_order(order: Order):
    order_id = str(uuid.uuid4())  # Generate a unique ID for the order
    order.id = order_id

    # Check if products in the order are available in sufficient quantity
    for item in order.items:
        product = products_collection.find_one({"_id": item.product_id})
        if product is None or product["quantity"] < item.bought_quantity:
            raise HTTPException(
                status_code=400, detail="Product not available or quantity exceeded")

    # Calculate the total amount for the order
    total_amount = sum(
        item.bought_quantity * product["price"]
        for item in order.items
    )

    # Create the order
    order.total_amount = total_amount
    orders_collection.insert_one(order.dict())
    return order


@app.get("/orders")
async def list_orders(limit: int = Query(default=10, ge=1), offset: int = Query(default=0, ge=0)):
    total_orders = orders_collection.count_documents({})
    orders = orders_collection.find({}).limit(limit).skip(offset)
    return {
        "total_orders": total_orders,
        "orders": [order for order in orders]
    }


@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    order = orders_collection.find_one({"_id": order_id})
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.put("/products/{product_id}")
async def update_product(product_id: str, product: Product):
    result = products_collection.update_one(
        {"_id": product_id}, {"$set": product.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return product.dict()
