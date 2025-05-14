FROM python:3.11-slim

# 1️⃣   Set env flags
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 2️⃣   Install app
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dockerfile / /code/

# 3️⃣   Run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]