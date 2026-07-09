### 🚀 DevOps Task Manager
A production-style DevOps project demonstrating CI/CD, Kubernetes, and GitOps using GitHub Actions, Docker and Argo CD.
This project automatically builds a Docker image, pushes it to Docker Hub, updates the kubernetes deployment manifest with an immutable GIT SHA image tag, and deploys the letest version to Kubernetes using Argo CD GitOps.

## 🛠 Tech Stack 
- Python 
- Flask
- Docker 
- Docker Hub 
- Kubernetes
- Minikube 
- GitHub Actions 
- Argo CD
- Git 

## 📖 Project Overview
The DevOps Task Manager is a Flask-based web application built to demonstrate a complete modern DevOps workflow.
The project follows GitOps principles where Git is the single source of truth.Every code change triggers an automated GitHub Actions workflow that: 
1. Build a Docker image 
2. Tags the image with current Git commit SHA 
3. Pushes the image to Docker Hub
4. Updates the kubernetes deployment manifest with the new image tag
5. Commits the updated manifest back to GitHub
6. Allows Argo CD to detect the Git change and automatically synchronize the kubernetes cluster 
This workflow demonstrates immutable deployments, automated rolling updates and production-style continuous delivery.
