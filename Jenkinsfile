pipeline {
    agent any

    environment {
        VM_IP = "192.168.31.33"
        VM_USER = "ubuntu"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/RambabuSoyam/docker-jenkins-demo.git'
            }
        }

        // 🔥 BACKEND DEPLOYMENT
        stage('Deploy Backend to VM') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no ${VM_USER}@${VM_IP} << EOF

                # Stop old app
                pkill -f app.py || true

                # Setup app directory
                mkdir -p ~/app
                cd ~/app

                # Clean old code
                rm -rf *

                exit
                EOF
                '''

                sh '''
                # Copy files to VM
                scp -r app/* ${VM_USER}@${VM_IP}:~/app/
                '''

                sh '''
                ssh ${VM_USER}@${VM_IP} << EOF

                cd ~/app

                # Install dependencies
                pip3 install -r requirements.txt --break-system-packages || true

                # Start app
                nohup python3 app.py > app.log 2>&1 &

                exit
                EOF
                '''
            }
        }

        // 🔥 FRONTEND + NGINX DEPLOYMENT
        stage('Deploy Frontend (Nginx)') {
            steps {
                sh '''
                docker stop nginx-container || true
                docker rm nginx-container || true

                docker run -d -p 80:80 \
                -v $(pwd)/index.html:/usr/share/nginx/html/index.html \
                -v $(pwd)/nginx.conf:/etc/nginx/conf.d/default.conf \
                --name nginx-container nginx
                '''
            }
        }

    }
}
