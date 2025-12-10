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
                sh 'docker run --rm relax-tests pylint tests pages || true'
            }
        }

         stage('Run Tests') {
            steps {
                sh 'mkdir -p ${WORKSPACE}/allure-results'
                sh '''
                    docker run --rm \
                        -v ${WORKSPACE}/allure-results:/app/allure-results \
                        relax-tests \
                        pytest --alluredir=/app/allure-results
                '''
                sh 'ls -l ${WORKSPACE}/allure-results'
            }
        }

//         stage('Run Tests') {
//             steps {
//                 sh '''
//                     docker run --rm \
//                         -v ${WORKSPACE}/allure-results:/app/allure-results \
//                         relax-tests \
//                         pytest --alluredir=/app/allure-results
//                 '''
//             }
//         }

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
    }
}
