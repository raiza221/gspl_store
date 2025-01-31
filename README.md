# Django JWT Authentication with SimpleJWT

This project demonstrates how to implement **JSON Web Token (JWT)** authentication in a Django application using the **Django Rest Framework** (DRF) and **Simple JWT**. The backend provides a set of API endpoints for user authentication, CRUD operations for products, and a custom permission class for handling authenticated users and token expiration.

## Features

- **JWT Authentication** using SimpleJWT.
- **Access and Refresh Tokens** for secure user authentication.
- **Custom Permission** for checking token expiration and managing access control.
- **Pagination, Filtering, and CRUD Operations** for products.
- **User Registration and Login** functionality.

## Requirements

- Python 3.13.1
- asgiref==3.8.1
- Django==5.0.11
- django-cors-headers==4.6.0
- django-filter==24.3
- django-mssql-backend==2.8.1
- djangorestframework==3.15.2
- djangorestframework_simplejwt==5.4.0
- mssql-django==1.5
- PyJWT==2.10.1
- pyodbc==5.2.0
- pytz==2024.2
- sqlparse==0.5.3
## Installation

Follow these steps to set up the project:

### Step Turoeial

```bash
git clone https://github.com/raiza221/gspl_store
python -m venv venv
source venv/bin/activate  
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


