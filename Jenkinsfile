pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8085:80 jenkins-demo'
            }
        }

    }
}
