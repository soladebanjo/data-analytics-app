pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Create virtual environment and upgrade pip
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && python3 -m pip install --upgrade pip'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    // Install dependencies in the virtual environment
                    sh '. venv/bin/activate && python3 -m pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests within the virtual environment
                    sh '. venv/bin/activate && python3 -m pytest'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    docker.build('my-python-app:latest')
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                // Deploy using kubectl
                sh 'kubectl apply -f k8sdeployment.yaml'
            }
        }
    }
}
