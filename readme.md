# BlockHouse Backend Service

This project is a simple backend service that exposes REST APIs for creating and retrieving trade orders, as well as providing real-time updates via WebSockets. The backend is built using FastAPI, with SQLite as the database. The application is containerized using Docker and deployed on an AWS EC2 instance. A CI/CD pipeline is set up using GitHub Actions.

## Features

- **Create Orders**: POST `/orders/` to submit a new order.
- **List Orders**: GET `/orders/` to retrieve the list of submitted orders.
- **WebSocket Updates**: A WebSocket endpoint to receive real-time updates on orders.
- **Database**: The service uses SQLite to store orders.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite
- **WebSockets**: For real-time updates
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Deployment**: AWS EC2

## Installation

### Prerequisites

- Python 3.9+
- Docker (for containerization)
- AWS EC2 (for deployment)
- GitHub Actions (for CI/CD)

### Set Up Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/blockhouse-backend.git
   cd blockhouse-backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application locally:

   ```bash
   uvicorn app.main:app --reload
   ```

5. The app will be accessible at `http://127.0.0.1:8000`.

### Docker Setup

To run the application inside Docker:

1. Build the Docker image:

   ```bash
   docker build -t trade-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 8000:8000 trade-app
   ```

3. The app will be accessible at `http://127.0.0.1:8000` inside the container.

### Deployment on AWS EC2

1. Launch an EC2 instance (Ubuntu).
2. Install Docker and Docker Compose on the EC2 instance.
3. Use `scp` to transfer your Docker setup and the app to the EC2 instance:

   ```bash
   scp -i your-key.pem -r . ubuntu@ec2-ip:/home/ubuntu/blockhouse-task
   ```

4. SSH into the EC2 instance and run:

   ```bash
   cd /home/ubuntu/blockhouse-task
   docker build -t trade-app .
   docker run -d -p 8000:8000 trade-app
   ```

## CI/CD Pipeline

This project is integrated with GitHub Actions to automatically run tests, build the Docker image, and deploy the app to an AWS EC2 instance upon a merge to the `main` branch.

### GitHub Actions Workflow

The workflow consists of two jobs:

- **Build**: Installs dependencies, runs tests with `pytest`.
- **Deploy**: Deploys the application to the EC2 instance after a successful build.

## References

1. [Blockhouse Assignment - Take Home](https://you.ashbyhq.com/blockhouse/assignment/100ee943-e9f5-48f2-ba60-b7163bc5b01f)
2. [FastAPI After the Getting Started](https://medium.com/@marcnealer/fastapi-after-the-getting-started-867ecaa99de9)
3. [FastAPI on_event decorator is deprecated](https://stackoverflow.com/questions/78042466/fastapi-app-on-event-decorator-is-deprecated-how-can-i-create-a-simple-repeat)
4. [Google Search: FAST API startup](https://www.google.com/search?q=FAST+API+startup&oq=FAST+API+startup&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTINCAEQABiRAhiABBiKBTIJCAIQABgKGIAEMgkIAxAAGAoYgAQyCQgEEAAYChiABDIJCAUQABgKGIAEMgkIBhAAGAoYgAQyCQgHEAAYChiABDIGCAgQRRg80gEINDkwM2owajSoAgCwAgE&sourceid=chrome&ie=UTF-8)
5. [FastAPI with SQL](https://medium.com/towards-data-engineering/fastapi-with-sql-1c7852ccbf21)
6. [Google Search: FAST API post](https://www.google.com/search?q=FAST+API+post&oq=FAST+API+post+&gs_lcrp=EgRlZGdlKgwIABBFGDkYgAQYogQyDAgAEEUYORiABBiiBDINCAEQABiRAhiABBiKBTIMCAIQABgUGIcCGIAEMgcIAxAAGIAEMgcIBBAAGIAEMg0IBRAAGIYDGIAEGIoFMg0IBhAAGIYDGIAEGIoFMg0IBxAAGIYDGIAEGIoF0gEJMTAwNjVqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8)
7. [FastAPI Body Tutorial](https://fastapi.tiangolo.com/tutorial/body/)
8. [Utilizing Databases in FastAPI Routers](https://www.vskills.in/certification/tutorial/utilizing-databases-in-fastapi-routers/)
9. [FastAPI SQL Databases Tutorial](https://fastapi.tiangolo.com/tutorial/sql-databases/)
10. [FastAPI Bigger Applications Tutorial](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
11. [Getting Started with WebSocket in FastAPI](https://medium.com/@nmjoshi/getting-started-websocket-with-fastapi-b41d244a2799)
12. [Testing FastAPI Application with Pytest](https://medium.com/@gnetkov/testing-fastapi-application-with-pytest-57080960fd62)
13. [FastAPI Testing with TestClient](https://fastapi.tiangolo.com/tutorial/testing/#using-testclient)
14. [Pytest Advanced FastAPI Testing](https://pytest-with-eric.com/pytest-advanced/pytest-fastapi-testing/)
15. [Google Search: Fast API and Pytest](https://www.google.com/search?q=fast+api+and+pytest&oq=fast+api+and+pytest&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIICAEQABgNGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigUyDQgGEAAYhgMYgAQYigUyCggHEAAYgAQYogQyBggIEEUYPNIBCDQ1NDlqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8)
16. [How to Exclude .git in SCP from GitHub Actions](https://www.google.com/search?q=how+to+exclu+.git+in+scp+from+gitactions&oq=how+to+exclu+.git+in+scp+from+gitactions&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIKCAEQABiABBiiBDIHCAIQABjvBTIHCAMQABjvBTIKCAQQABiABBiiBNIBCTExNjUwajBqMagCALACAA&sourceid=chrome&ie=UTF-8)
