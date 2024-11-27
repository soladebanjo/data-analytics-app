pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Activate the virtual environment
                    sh '. venv/bin/activate && python3 -m pip install --upgrade pip'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    // Use the virtual environment to install dependencies
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
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
