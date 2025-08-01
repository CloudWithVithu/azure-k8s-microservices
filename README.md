# 🚀 Azure Kubernetes Microservices Project

This project is a production-grade, containerized microservices application deployed on **Azure Kubernetes Service (AKS)**. It showcases a full-stack solution with a **Node.js frontend**, **Python Flask backend**, and **MongoDB** as the database, all orchestrated via Kubernetes and deployed using automated CI/CD pipelines.

This reflects my comprehensive understanding of cloud-native architecture, containerization, Kubernetes orchestration, and DevOps automation on Azure.

---

## 🧩 Project Summary

The application consists of:

- **Frontend:** Node.js Express server running on port 3000 serving user-facing pages and calling backend APIs.
- **Backend:** Python Flask REST API connected to MongoDB for persistent data management.
- **Database:** MongoDB deployed as a Kubernetes service within the cluster.
- **Infrastructure:** AKS for container orchestration, Azure Container Registry (ACR) for image hosting.
- **CI/CD:** GitHub Actions automate Docker image builds, push to ACR, and deployment updates to AKS with zero downtime.

---

## ✅ Main Highlights

- Microservices architecture using containers and Kubernetes for scalability and resilience.
- Full Dockerization of frontend and backend services.
- Kubernetes manifests managing deployments, services, and LoadBalancer exposure.
- Secure Azure authentication using service principal and GitHub secrets.
- Automated CI/CD pipelines for build, push, and rolling update deployments using GitHub Actions.
- Environment variables and service discovery implemented for smooth MongoDB integration.
- Modular project structure enabling easier development and maintenance.

---

## 🛠️ Tech Stack

| Category        | Technologies Used                       |
|-----------------|---------------------------------------|
| Cloud Infra     | Azure Kubernetes Service (AKS), ACR    |
| Containerization| Docker                                |
| Orchestration   | Kubernetes (Deployments, Services)    |
| Backend        | Python Flask, PyMongo                   |
| Frontend       | Node.js, Express                        |
| Database       | MongoDB (containerized in AKS)          |
| CI/CD          | GitHub Actions, Azure CLI, Docker Login |

---

## 📁 Folder Structure

azure-k8s-microservices/
├── backend/ # Flask backend + Dockerfile
├── frontend/ # Node.js frontend + Dockerfile
├── k8s-manifests/ # Kubernetes YAML manifests for deployments and services
├── .github/workflows/ # GitHub Actions workflows for CI/CD
├── README.md
└── ...


---

## 🔄 CI/CD Automation

- Builds Docker images for backend and frontend on every push.
- Pushes images to Azure Container Registry tagged with Git commit SHA.
- Updates AKS deployments to new images with rolling update strategy.
- Uses secure Azure service principal authentication with secrets stored in GitHub.
- Automates environment consistency and fast iteration from code push to deployment.

---

## 🧪 Testing & Verification

- Manual endpoint testing via `curl` or browser to verify frontend and backend APIs.
- Kubernetes `kubectl` commands for pod, service, and rollout status monitoring.
- Logs examined to troubleshoot container startup and runtime errors.
- CI/CD workflow includes rollout status checks to ensure healthy deployment.

---

## 📈 Future Enhancements

- Integrate an ingress controller (e.g., NGINX) for hostname routing and HTTPS.
- Add monitoring and alerting with Prometheus and Grafana.
- Implement Helm charts for simplified deployment and versioning.
- Add authentication and authorization with Azure AD or JWT.
- Expand backend functionality and frontend UI for richer user experience.

---

## 🙌 Final Notes

This project represents a real-world, end-to-end microservices deployment on Azure with Kubernetes orchestration and DevOps automation. It highlights practical skills in cloud infrastructure, container orchestration, CI/CD pipelines, and application development.

---

## Author

Vithushan — Aspiring Cloud Engineer | DevOps Enthusiast | Kubernetes Practitioner

---
