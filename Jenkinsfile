pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'banking-system-app'
        DOCKER_REGISTRY = 'your-dockerhub-username'
        AWS_REGION = 'us-east-1'
        CLUSTER_NAME = 'my-k8s-cluster'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "Checking out code..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                sh "docker build -t ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${env.BUILD_NUMBER} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker Image to DockerHub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                    echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin
                    docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                sh """
                aws eks --region ${AWS_REGION} update-kubeconfig --name ${CLUSTER_NAME}
                kubectl apply -f k8s-deployment.yaml
                kubectl set image deployment/banking-deployment banking-container=${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}
