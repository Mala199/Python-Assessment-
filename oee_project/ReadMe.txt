

# OEE Project

This is a Django web application for managing OEE (Overall Equipment Effectiveness) data for machines.

## Features

- CRUD operations for machines
- Calculation of OEE metrics
- User authentication and authorization
- RESTful API for machine data

## Installation


Install dependencies


Apply database migrations


python manage.py migrate


Create a superuser (admin) account:


python manage.py createsuperuser


 Run the development server:


python manage.py runserver


 Access the application in your web browser at `http://127.0.0.1:8000/`

## Usage

- Access the admin interface at `http://127.0.0.1:8000/admin/` to manage machines and users.
- Use the RESTful API endpoints for machine data.
- Implement frontend views and templates as needed for your specific use case.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.




