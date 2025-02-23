FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Expose port 8000
EXPOSE 8000

CMD pip install -r requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 8000
