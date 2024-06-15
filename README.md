# Django Practice Project

- Basic Django Modeling, API design, and implementation using Django
- This project demonstrates basic CI/CD practices.

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
```

Log in with the superuser account you created.
