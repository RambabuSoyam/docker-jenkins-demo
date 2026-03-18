pipeline {
    agent any

    environment{
        IMAGE_NAME='jenkins-demo'
        CONTAINER_NAME='jenkins-container'
        PORT='8085'
    }
    stages {

        stage('Checkout code') {
            steps {
                echo "cloning repo..."
            }
        }

        stage('Verify files') {
            steps {
                sh 'ls -lrt'
            }
        }
        stage('Build Docker Image'){
            steps{
                echo "Building Docker Image....."
                sh 'docker build -t $IMAGE_NAME .'
            }
    }
        stage('Stop Old Container'){
            steps{
                echo "Stopping old container if exists..."
                sh 'docker rm -f $CONTAINER_NAME || true'
            }
        }
        stage('Run New Container'){
            steps{
                echo "Running new container..."
                sh '''
                docker run -d -p $PORT:80 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
      stage('Health Check') {
            steps {
                echo "Checking application health..."
                sh '''
                sleep 5
                curl -f http://localhost:$PORT || exit 1
                '''
            }
        }
       post{
           success{
               echo "Deployment Successful"
       }     
           failure{
               echo"Deployment failed"
           }
       }
}
}
