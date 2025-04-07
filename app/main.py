from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.campaign import router as campaign_router
from app.api.customer import router as customer_router

app = FastAPI(
    title="GP Test Project",
    version="0.1.0",
    description="FastAPI project with PostgreSQL, Redis, Celery, Alembic and SQLAlchemy",
    debug=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(campaign_router)
app.include_router(customer_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}