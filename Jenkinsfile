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

        stage('Build') {
            steps {
                echo 'CloudCare build stage started'
            }
        }

        stage('Test') {
            steps {
                echo 'CloudCare testing stage started'
            }
        }
    }
}
