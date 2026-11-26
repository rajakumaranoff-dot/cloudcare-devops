
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

        
        stage('Deploy') {
            steps {
                withCredentials([
                    string(credentialsId: 'cloudcare-db-user', variable: 'POSTGRES_USER'),
                    string(credentialsId: 'cloudcare-db-password', variable: 'POSTGRES_PASSWORD'),
                    string(credentialsId: 'cloudcare-db-name', variable: 'POSTGRES_DB')
                        ]) {
                            sh '''
                                docker rm -f cloudcare-app || true

                                docker run -d \
                                    --name cloudcare-app \
                                    --network aws-devops-portfolio_default \
                                    -p 5003:5000 \
                                    -e DB_HOST=db \
                                    -e DB_PORT=5432 \
                                    -e POSTGRES_USER \
                                    -e POSTGRES_PASSWORD \
                                    -e POSTGRES_DB \
                                    cloudcare-app:latest
                                '''
            }
        }
    }

}
