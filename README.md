
````markdown
# Flask Kubernetes CI/CD Pipeline

This project demonstrates how to:
- Build a Flask app
- Containerize it with Docker
- Deploy it to Kubernetes (Minikube)
- Automate the process using GitHub Actions with a self-hosted Windows runner

## 🔧 Technologies Used
- Python + Flask
- Docker
- Kubernetes (Minikube)
- GitHub Actions

## 🛠️ Setup

### 1. Run Minikube Locally
```bash
minikube start
````

### 2. Self-Hosted GitHub Runner

* Register a Windows self-hosted runner with your repo
* Run `run.cmd` to activate it

### 3. Push Code to Trigger Pipeline

```bash
git push origin main
```

## 🖥️ Deployment

The app will be deployed to your Minikube cluster. Access it via:

```bash
minikube service flask-service
```

## 🔗 Result

The application will return:

```text
Hello from Flask app deployed using Kubernetes!
```

