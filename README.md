# 🚀 AI Task Processing Platform

A production-ready full-stack AI task processing platform built using MERN stack, Python worker, Redis queue, Docker, Kubernetes, Argo CD, and CI/CD.

This platform allows users to create text-processing AI tasks and process them asynchronously in the background with real-time task tracking.

---

## 📌 Features

- User registration and login using JWT authentication
- Create AI tasks with title, input text, and operation
- Supported operations:
  - Uppercase
  - Lowercase
  - Reverse String
  - Word Count
- Background task processing using Python worker
- Redis queue integration
- Task status tracking:
  - Pending
  - Running
  - Success
  - Failed
- View task logs and results
- Dockerized services
- Kubernetes deployment support
- GitOps using Argo CD
- CI/CD pipeline using GitHub Actions

---

## 🛠️ Tech Stack

### 🎨 Frontend
- React / Next.js
- Axios
- Tailwind CSS

### ⚙️ Backend
- Node.js
- Express.js
- MongoDB
- JWT Authentication
- bcrypt
- Helmet
- Express Rate Limit

### 🤖 Worker
- Python
- Redis Queue

### ☁️ DevOps
- Docker
- Docker Compose
- Kubernetes
- Argo CD
- GitHub Actions

---

## 🏗️ System Architecture

```text
Frontend (React / Next.js)
        |
        v
Backend API (Node.js + Express)
        |
        v
MongoDB -------- Redis Queue
                    |
                    v
            Python Worker Service


## 📂 Project Structure

ai-task-platform/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── backend/
├── frontend/
├── worker/
├── k8s/
├── docker-compose.yml
├── README.md
├── architecture-document.pdf
└── screenshots/

🔐 Environment Variables
Create separate .env files for frontend, backend, and worker services.

⚙️ Backend .env
Environment
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=vourful
REDIS_HOST=redis
REDIS_PORT=6379

🎨 Frontend .env
Environment
REACT_APP_API_URL=http://localhost:5000

🤖 Worker .env
Environment
REDIS_HOST=redis
REDIS_PORT=6379
MONGO_URI=your_mongodb_connection_string
💻 Run Project Locally
📥 Clone the Repository

git clone https://github.com/Vasundhara-02/ai-task-platform.git
cd ai-task-platform
🐳 Run Using Docker Compose

docker-compose up --build
🛑 Stop All Running CContainerization
docker-compose down

☸️
 Kubernetes Deployment
📦 Create Namespace
kubectl apply -f k8s/namespace.yaml

🚀 Deploy All Services
kubectl apply -f k8s/
✅ Verify Pods
kubectl get pods -n ai-task-platform

✅ Verify Services
kubectl get svc -n ai-task-platform

🔄 Argo CD Setup
📥 Install Argo CD

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

🚀 Apply Argo CD Application

kubectl apply -f argocd-application.yaml

✅ Verify Argo CD Application

kubectl get applications -n argocd

🔁 CI/CD Pipeline
The GitHub Actions workflow automates the following steps:
Install dependencies
Run lint checks
Build Docker images
Push Docker images to Docker Hub
Update Kubernetes image tags
Trigger deployment through Argo CD

🛡️ Security Features
JWT-based user authentication
Password hashing using bcrypt
Helmet middleware for securing HTTP headers
Rate limiting to prevent abuse
Environment variable-based secret management
Non-root Docker containers for improved security

📈 Scaling Strategy
Worker service supports horizontal scaling
Multiple worker replicas can process Redis queue jobs simultaneously
Kubernetes resource limits and readiness probes are configured
The architecture is designed to support high-volume task processing

📸 Screenshots
Added project screenshots inside the screenshots/ folder:
Login Page
Register Page
Dashboard
Task Creation Page
Task Result Page
Docker Containers Running
Kubernetes Pods
Argo CD Dashboard

🌐 Live Deployment
Frontend URL: http://127.0.0.1:40555 (Minikube local)
Backend URL: http://localhost:3000

==== 👩‍ Author ====
  Vasundara Nadar
