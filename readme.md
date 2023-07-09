# Ecommerce Application

This is an ecommerce application built using FastAPI and MongoDB.

## Features

- List all available products
- Create a new order
- Fetch all orders with pagination support
- Fetch a single order by ID
- Update product quantity

## Requirements

- Python 3.7+
- MongoDB

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/ecommerce-app.git
cd ecommerce-app


The FastAPI server should now be running at http://localhost:8000.

API Endpoints
List all available products
URL: /products
Method: GET
Description: Get a list of all available products.
Create a new product
URL: /products
Method: POST
Description: Create a new product.
Request Body:
name (string): Name of the product.
price (float): Price of the product.
quantity (int): Available quantity of the product.
Create a new order
URL: /orders
Method: POST
Description: Create a new order.
Request Body:
timestamp (string): Timestamp of the order.
items (list of objects): List of items bought in the order.
product_id (int): ID of the product.
bought_quantity (int): Quantity of the product bought.
user_address (object): User address details.
city (string): City of the user.
country (string): Country of the user.
zip_code (string): Zip code of the user.
Fetch all orders
URL: /orders
Method: GET
Description: Get a paginated list of all orders.
Query Parameters:
limit (optional, integer): Number of orders to return per page (default: 10).
offset (optional, integer): Offset of orders (default: 0).
Fetch a single order
URL: /orders/{order_id}
Method: GET
Description: Get a single order by ID.
Path Parameter:
order_id (string): ID of the order to retrieve.
Update product quantity
URL: /products/{product_id}
Method: PUT
Description: Update the quantity of a product.
Path Parameter:
product_id (string): ID of the product to update.
Request Body:
quantity (int): Updated quantity of the product.
Refer to the API documentation for detailed request and response examples.

Database
This application uses MongoDB as the database for storing products and orders. Make sure you have MongoDB installed and running locally. Update the MongoDB connection details in main.py if needed.








