# Django Practice Project

- Basic Django Modeling, API design, and implementation using Django
- This project demonstrates basic CI/CD practices.


# Technology Stack
- Python: The programming language used for developing the application.
- Django: The web framework used for building the backend of the application.
- Django Rest Framework (DRF): An extension of Django for building RESTful APIs.
- PostgreSQL: The database system used for storing application data.
- Docker: A platform for developing, shipping, and running applications in containers.
- Nginx: A web server used as a reverse proxy to serve the Django application.
- Amazon EC2: The cloud computing service used to deploy and run the application.

## Project Structure
```bash
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-312.pyc
│   ├── chat
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── consumers.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── routing.py
│   │   ├── templates
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── comments
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── common
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── test.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── management
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── reactions
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── static
│   ├── storage
│   ├── subscriptions
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── users
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   └── views.py
│   └── videos
│       ├── __init__.py
│       ├── __pycache__
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── data
│   └── db  [error opening dir]
├── docker-compose-deploy.yml
├── docker-compose.yml
├── proxy
│   ├── Dockerfile
│   ├── default.conf.tpl
│   ├── run.sh
│   └── uwsgi_params
├── requirements.dev.txt
├── requirements.txt
└── scripts
    └── run.sh
```

## How to Install

### 1. Clone the Project

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create .env File

Create a `.env` file in the project root directory:

```bash
vim .env
```

### 3. Populate the .env File

The `.env` file must contain the following environment variables. Note that since we are using a Docker Compose setup for the database, actual database server details are not required.

```env
DOCKER_ACCESS_TOKEN=YOURDOCKERACCESSTOKEN  # (Optional)
DB_NAME=youtube
DB_USER=test
DB_PASS=123123
DJANGO_SECRET_KEY=test
DJANGO_ALLOWED_HOSTS=YOUR_EC2_DOMAIN_NAME
```

### 4. Start Docker Compose

Ensure Docker is installed on your EC2 instance. Then, build and start the Docker containers:

```bash
docker-compose -f docker-compose-deploy.yml up -d --build
```

### 5. Create Superuser

Run the following command to create a Django superuser:

```bash
docker-compose -f docker-compose-deploy.yml run --rm app sh -c 'python manage.py createsuperuser'
```

### 6. Access the Web Application

Connect to your EC2 instance using your web browser:

```
http://your-ec2-instance/admin
http://your-ec2-instance/api/v1/schema/swagger-ui
http://your-ec2-instance/chat
```

Log in with the superuser account you created.
