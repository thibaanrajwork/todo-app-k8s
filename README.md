# Todo App — Kubernetes GitOps Pipeline

A simple Flask to-do API deployed end-to-end using a full GitOps workflow: Docker → Kubernetes (k3s) → Helm → ArgoCD.

## What this demonstrates

- Containerizing a Python/Flask application with Docker
- Deploying to Kubernetes using a Helm chart (templated, configurable deployment)
- GitOps continuous deployment with ArgoCD — pushing to `main` automatically triggers a rolling update, no manual `kubectl`/`helm` commands needed
- Kubernetes health checks (liveness/readiness probes) wired to a dedicated `/health` endpoint

## Architecture

Code change → git push → GitHub → ArgoCD detects change → Helm chart applied → Kubernetes rolling update → new pod live

ArgoCD continuously watches this repository. Any change to `todo-chart/` is automatically synced to the cluster — git is the single source of truth for what's running.

## Tech Stack

| Layer | Tool |
|---|---|
| Application | Python / Flask |
| Containerization | Docker |
| Orchestration | Kubernetes (k3s) |
| Deployment packaging | Helm |
| Continuous deployment | ArgoCD (GitOps) |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health/status message |
| GET | `/todos` | List all to-dos |
| POST | `/todos` | Create a new to-do |
| GET | `/health` | Kubernetes health check endpoint |

## Running Locally

docker build -t todo-app:v2 .
docker run -d -p 5000:5000 todo-app:v2
curl http://localhost:5000

## Deploying to Kubernetes (k3s)

docker save todo-app:v2 -o todo-app.tar
sudo k3s ctr images import todo-app.tar
helm install todo-release ./todo-chart

## GitOps Deployment (ArgoCD)

Once an ArgoCD Application is pointed at this repo's `todo-chart/` path with automatic sync enabled, any commit to `values.yaml` (e.g. bumping the image tag) triggers an automatic rolling deployment.

## Project Structure

- app.py — Flask application
- Dockerfile — Container build instructions
- requirements.txt — Python dependencies
- todo-chart/ — Helm chart for Kubernetes deployment
  - Chart.yaml
  - values.yaml — Configurable settings (image tag, port, probes)
  - templates/ — Kubernetes manifest templates
