
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Code-Ace666/aws-devops-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'venv/bin/python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aws-devops-app:v1 .'
            }
        }
    }
}
