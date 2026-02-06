pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/teu-username/teu-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-api .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm django-api python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }

    post {
        success {
            echo 'Deploy realizado com sucesso!'
        }
        failure {
            echo 'Falha no pipeline!'
        }
    }
}
