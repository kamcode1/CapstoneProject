
# E-commerce Product API

## Overview

This project is a fully functional e-commerce product management API built using Django and Django REST Framework. It allows for creating, reading, updating, and deleting products, user management, and user authentication via JSON Web Tokens (JWT). It also includes basic features like adding items to a cart and managing stock quantity for products.

### Features

- **Product Management (CRUD)**
  - Create, Read, Update, and Delete products
  - Each product has attributes like name, description, price, category, stock quantity, and image URL.
  - Stock quantity automatically updates when an order is placed.
  
- **User Management (CRUD)**
  - Create, Read, Update, and Delete users.
  - Users have a role of either `seller` or `buyer`.
  - Only authenticated users can manage products.
  
- **Cart Management**
  - Buyers can add products to their cart.
  - Stock quantity is reduced when products are added to the cart.
  
- **Authentication**
  - Token-based authentication using JWT (JSON Web Tokens).
  - Login and token refreshing capabilities.

## Technologies

- **Backend Framework**: Django, Django REST Framework
- **Authentication**: JWT (JSON Web Token)
- **Database**: MySQL
- **Python version**: 3.12

## Requirements

- Python 3.12 or higher
- Django 5.0.6
- Django REST Framework
- MySQL
- Django SimpleJWT for authentication

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
```

### 2. Install Dependencies

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database

Make sure you have MySQL installed and running. Create a MySQL database named `ecommerce_db`.

```sql
CREATE DATABASE ecommerce_db;
```

In your `settings.py`, configure the database connection:

```python
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',
        'USER': 'root',
        'PASSWORD': 'YourPasswordHere',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Apply Migrations

Run the migrations to set up the database tables:

```bash
python manage.py migrate
```

### 5. Create Superuser

Create a superuser to access the Django Admin Panel:

```bash
python manage.py createsuperuser
```

### 6. Run the Server

You can now start the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin` to access the admin panel and `http://127.0.0.1:8000/api/` for API endpoints.

## API Endpoints

### User Endpoints

- **Register a new user**: `POST /api/users/`
- **List all users**: `GET /api/users/`
- **Login**: `POST /api/token/`
- **Token refresh**: `POST /api/token/refresh/`

### Product Endpoints

- **List all products**: `GET /api/products/`
- **Create a new product**: `POST /api/products/` (authenticated sellers only)
- **Update a product**: `PUT /api/products/<id>/` (authenticated sellers only)
- **Delete a product**: `DELETE /api/products/<id>/` (authenticated sellers only)

### Cart Endpoints

- **Add a product to the cart**: `POST /api/cart/items/`
- **View cart**: `GET /api/cart/`

## Authentication

This API uses JWT for authentication. After registering or logging in, you will receive a token that must be included in the `Authorization` header for all authenticated requests.

### Example

```
Authorization: Bearer <your-token-here>
```

## Folder Structure

```bash
ecommerce_api/
├── core/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── serializers.py
├── products/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── users/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── ecommerce_api/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── manage.py
```

## Tests

To run tests for the project:

```bash
python manage.py test
```

## Future Enhancements

- **Wishlist Functionality**: Allow buyers to add products to a wishlist.
- **Product Reviews**: Enable product reviews by buyers.
- **Advanced Stock Management**: Automate stock reduction upon purchase.


## Contact

For any inquiries or issues, please reach out to the project maintainer at [kamnoah88@gmail.com].
