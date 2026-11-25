pipeline {
    agent any

    stages {
        stage('Welcome') {
            steps {
                echo 'Welcome to CloudCare CI/CD!'
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
                echo 'CloudCare source code checked out successfully!'
            }
        }

            stage('Build Docker Image') {
                steps {
                    sh 'docker build -t cloudcare-app:latest .'
            }
        }

        stage('Test') {
            steps {
                echo 'CloudCare testing stage started'
            }
        }
    }
}
