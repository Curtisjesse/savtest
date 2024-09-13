Savannah Informatics Backend Challenge
This project is a Django-based REST API for managing customers and orders, including SMS notifications for new orders.
Features

Customer management (CRUD operations)

Order management (CRUD operations)

SMS notifications for new orders using Africa's Talking API

Authentication and authorization using OpenID Connect

Unit tests for all main functionalities

CI/CD pipeline using GitHub Actions


Setup

Clone the repository:

git clone https://github.com/Curtisjesse/savtest.git

cd savtest


Create a virtual environment and activate it:

python -m venv venv

source venv/bin/activate  # On Windows use   venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

Set up environment variables:

Create a .env file in the project root and add the following:

MYSQL_DATABASE=Savannah

MYSQL_USER='postgres'

MYSQL_PASSWORD=your_password

MYSQL_HOST=localhost

MYSQL_PORT=5432

ALLOWED_HOSTS=localhost,127.0.0.1

DEBUG=True

SECRET_KEY=your_secret_key

AFRICASTALKING_USERNAME=your_username

AFRICASTALKING_API_KEY=your_api_key

make migrations:

python manage.py makemigrations

Run migrations:

python manage.py migrate

Run the development server:

python manage.py runserver


Running Tests

To run the test suite:

python manage.py test

API Endpoints

/api/customers/: Customer CRUD operations

/api/orders/: Order CRUD operations

Deployment

This project is set up for automatic deployment to Heroku via GitHub Actions. Push to the main branch to trigger the CI/CD pipeline.
