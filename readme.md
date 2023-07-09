

```markdown
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

Follow the instructions below to set up and run the Ecommerce Application on your local machine.

### Clone the repository

1. Open a terminal and navigate to the directory where you want to clone the repository.

2. Clone the repository using the following command:

```bash
git clone https://github.com/your-username/ecommerce-app.git
```

3. Change into the project directory:

```bash
cd ecommerce-app
```

### Set up the environment

1. Create a virtual environment (optional but recommended):

```bash
python3 -m venv env
```

2. Activate the virtual environment:

```bash
# For Linux/Mac
source env/bin/activate

# For Windows
.\env\Scripts\activate
```

### Install dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Start MongoDB server

Make sure MongoDB is installed and running on your local machine.

### Configure MongoDB connection

1. Open the `main.py` file in a text editor.

2. Update the MongoDB connection details (`mongodb://localhost:27017`) if your MongoDB server is running on a different host or port.

### Run the application

Start the FastAPI server using the following command:

```bash
uvicorn main:app --reload
```

The FastAPI server should now be running at http://localhost:8000.

## API Endpoints

The following API endpoints are available:

### List all available products

- **URL**: `/products`
- **Method**: GET
- **Description**: Get a list of all available products.

### Create a new product

- **URL**: `/products`
- **Method**: POST
- **Description**: Create a new product.
- **Request Body**:
  - `name` (string): Name of the product.
  - `price` (float): Price of the product.
  - `quantity` (int): Available quantity of the product.

### Create a new order

- **URL**: `/orders`
- **Method**: POST
- **Description**: Create a new order.
- **Request Body**:
  - `timestamp` (string): Timestamp of the order.
  - `items` (list of objects): List of items bought in the order.
    - `product_id` (int): ID of the product.
    - `bought_quantity` (int): Quantity of the product bought.
  - `user_address` (object): User address details.
    - `city` (string): City of the user.
    - `country` (string): Country of the user.
    - `zip_code` (string): Zip code of the user.

### Fetch all orders

- **URL**: `/orders`
- **Method**: GET
- **Description**: Get a paginated list of all orders.
- **Query Parameters**:
  - `limit` (optional, integer): Number of orders to return per page (default: 10).
  - `offset` (optional, integer): Offset of orders (default: 0).

### Fetch a single order

- **URL**: `/orders/{order_id}`
- **Method**: GET
- **Description**: Get a single order by ID.
- **Path Parameter**:
  - `order_id` (string): ID of the order to retrieve.

### Update product quantity

- **URL**: `/products/{product_id}`
- **Method**: PUT
- **Description**: Update the quantity of a product.
- **Path Parameter**:
  - `product_id` (string): ID of the product to update.
- **Request Body**:
  - `quantity` (int): Updated quantity of the product.

Refer to the API documentation for detailed request and response examples.

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to modify and customize the README file further based on your specific application and project requirements.