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


=======👩‍ Author =======
    Vasundhara Nadar
