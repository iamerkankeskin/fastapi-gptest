# GPTest Project

An advertising campaign platform where customers are called on a specific date and time and 30-second audio recordings are played. The platform can call many users at the same time during busy campaign periods.

## Technology Stack

- **FastAPI**: Modern, fast web API framework
- **PostgreSQL**: Relational database
- **Redis**: Used as cache and Celery broker
- **Celery**: Asynchronous task manager
- **Alembic**: Database migrations
- **SQLAlchemy**: ORM (Object-Relational Mapping)
- **Docker and Docker Compose**: Containerization

## Getting Started

### Requirements

- Docker and Docker Compose

### Installation

1. Clone the project:
```bash
git https://github.com/iamerkankeskin/fastapi-gptest.git
cd gptest
```

2. Configure the `.env` file (if necessary):
```
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/fastapi_db
REDIS_URL=redis://redis:6379/0
APP_NAME=GPTest Project
ENVIRONMENT=development
DEBUG=True
```

3. Run with Docker:
```bash
docker-compose up -d
```

4. The API will be accessible at: http://localhost:8000

### Alembic Migrations

To create a new migration:

```bash
docker-compose exec api alembic revision --autogenerate -m "migration description"
```

To apply migrations:

```bash
docker-compose exec api alembic upgrade head
```

## Usage

### API Documentation

API documentation is available at the following URLs:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Celery Tasks

To add a new task:

1. Create a new task file in the `app/tasks/` directory
2. Add it to the `include` list in the `app/tasks/celery_app.py` file
3. Trigger the task through the API

## Development

### Project Structure

```
fastapi-project/
├── alembic/              # Database migrations
├── app/                  # Main application directory
│   ├── api/              # API routes
│   ├── db/               # Database related code
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── tasks/            # Celery tasks
│   └── main.py           # Main FastAPI application
├── .env                  # Environment variables
├── alembic.ini           # Alembic configuration
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Docker configuration
└── requirements.txt      # Python dependencies
```