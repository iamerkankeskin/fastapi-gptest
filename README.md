# FastAPI Project

This project is an API built using FastAPI, PostgreSQL, Redis, Celery, Alembic, and SQLAlchemy.

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
git clone https://your-repository-url.git
cd fastapi-project
```

2. Configure the `.env` file (if necessary):
```
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/fastapi_db
REDIS_URL=redis://redis:6379/0
APP_NAME=FastAPI Project
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
│   ├── core/             # Core settings and configuration
│   ├── db/               # Database related code
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   ├── tasks/            # Celery tasks
│   └── main.py           # Main FastAPI application
├── tests/                # Tests
├── .env                  # Environment variables
├── alembic.ini           # Alembic configuration
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Docker configuration
└── requirements.txt      # Python dependencies
```