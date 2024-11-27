# Data Analytics Application

## Project Overview

This project is a Python-based data analytics application that performs basic statistical computations on a dataset. It includes a Flask-based web interface, a CI/CD pipeline for automation, and deployment using Docker and Kubernetes. Configuration management is achieved through tools like Ansible

---
## Setup and Deployment

### Features

1. **Data Analytics**: Calculates key statistics (mean, median, standard deviation).
2. **Web Interface**: Displays results using Flask.
3. **Automated CI/CD Pipeline**: Utilizes Jenkins for automated builds and testing.
4. **Containerization**: Docker-based deployment.
5. **Orchestration**: Minikube for Kubernetes-based deployment.
6. **Configuration Management**: Automates setup with Ansible

---

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/data-analytics-app.git
   cd data-analytics-app
   ```

2. **Set up a virtual environment and install dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the application locally**:
   ```bash
   python src/app.py
   ```

---

### Containerization with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t data-analytics-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 data-analytics-app
   ```

---

### Deployment on Kubernetes (Minikube)

1. **Start Minikube**:
   ```bash
   minikube start
   ```

2. **Configure Minikube to use local Docker images**:
   ```bash
   eval $(minikube docker-env)
   ```

3. **Build the Docker image for Minikube**:
   ```bash
   docker build -t my-python-app:latest .
   ```

4. **Apply Kubernetes manifests**:
   ```bash
   kubectl apply -f k8s/k8sdeployment.yaml
   kubectl apply -f k8s/k8sservice.yaml
   ```

5. **Access the application via Minikube**:
   ```bash
   minikube service myapp-service
   ```

---

### CI/CD Pipeline with Jenkins

1. **Set up Jenkins** on your machine.
2. Add a new Pipeline job pointing to the repository.
3. Use the provided `Jenkinsfile` to automate build, test, and deploy processes.

---

### Configuration Management with Ansible

1. **Install Ansible**:
   ```bash
   brew install ansible
   ```

2. **Set up a hosts inventory file** (e.g., `hosts`):
   ```ini
   [all]
   localhost ansible_connection=local
   ```

3. **Run the playbook**:
   ```bash
   ansible-playbook ansible/deploy.yaml -i hosts --ask-become-pass
   ```

---

## Testing

### Unit Tests

Run unit tests using Pytest:
```bash
pytest tests/
```

---

## Contribution Guidelines

Contributions are welcome! Follow these steps:

1. **Fork the repository**.
2. **Create a feature branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit changes**:
   ```bash
   git commit -m "Add feature description"
   ```
4. **Push to your fork**:
   ```bash
   git push origin feature-name
   ```
5. **Create a Pull Request**.

---

## License

This project is licensed under the [MIT License](LICENSE).
