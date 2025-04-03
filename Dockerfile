FROM python:3.13-slim

WORKDIR /app

# Sistem bağımlılıklarını yükleme
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıklarını yükleme
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyalama
COPY . .

# Alembic migrasyonlarını çalıştırma
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]