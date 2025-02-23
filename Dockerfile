FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install Python dependencies

# Expose port 8000
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
