Assignment
Work Trial Task

Task Overview:
You will build a simple backend service that exposes REST APIs, containerize the application using Docker, deploy it on an AWS EC2 instance, and set up a CI/CD pipeline using GitHub Actions.

Technical Requirements:
Backend Development (Python & Golang)

Build a simple REST API in either Python (FastAPI) or Golang (Gin/Echo) that:

Accepts trade order details (e.g., symbol, price, quantity, order type) via POST /orders.

Returns the list of submitted orders via GET /orders.

Stores order data in PostgreSQL or SQLite (for simplicity).

Bonus:

Implement WebSocket support for real-time order status updates.

DevOps & Deployment (AWS EC2 + Docker)
Containerization

Write a Dockerfile to containerize the application.

Use Docker Compose (optional) for local multi-container setup.

Deploy on AWS EC2

Launch an EC2 instance (Ubuntu).

Set up Docker and PostgreSQL on EC2.

Deploy the containerized backend service.

CI/CD with GitHub Actions

Set up a GitHub Actions workflow to:

Run tests on PRs.

Build the container image.

SSH into the EC2 instance and deploy the latest version on merge to main.

Expected Deliverables:
GitHub repo with well-structured code and README.

API documentation (Swagger/OpenAPI is a plus).

CI/CD pipeline configuration.

A short video (5-10 min) explaining your solution and approach.

Evaluation Criteria:
Clean, efficient backend code (Python/Golang).

Proper use of Docker for deployment.

Functioning CI/CD pipeline using GitHub Actions.

API correctness and handling edge cases.
