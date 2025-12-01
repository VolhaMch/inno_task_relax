// “CI triggered by Git push using GitHub webhook”
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t relax-tests .'
            }
        }

        stage('Lint') {
            steps {
                sh 'docker run --rm relax-tests pylint tests pages'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm -v $PWD/allure-results:/app/allure-results relax-tests pytest --alluredir=allure-results'
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

     post {
        always {
            cleanWs()
        }
        success {
            echo "✅ Pipeline completed successfully"
        }
        failure {
            echo "❌ Pipeline failed — check logs and Allure report"
        }
    }
}

