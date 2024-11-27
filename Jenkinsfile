pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Ensure pytest is installed
                    sh 'pip install pytest'
                    // Run tests
                    sh 'pytest'
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
                    // Apply Kubernetes deployment
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}

