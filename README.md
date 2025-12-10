# CI/CD for Python + Playwright using Jenkins in Docker

This project demonstrates a complete CI pipeline using:

- Jenkins running in Docker
- Dockerized test environment
- Pytest + Playwright tests
- Pylint for linting
- Allure Report generation

## Dockerfile
Creates a full isolated environment for running Playwright tests.

## Jenkinsfile
Pipeline stages:
1. Checkout
2. Build Docker image
3. Lint (pylint)
4. Run Tests (pytest)
5. Generate Allure Report

All tests are executed inside Docker containers.

## ▶How to run Jenkins locally

1. Create a custom Jenkins image with Docker CLI

    Go to  jenkins-docker, run command: docker build -t jenkins-docker-cli . 

2. Launch jenkins container

    Go to root, run command: docker run -d --name jenkins -p 8081:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --user root jenkins-docker-cli

3. Set up jenkins
    Open in browser: http://localhost:8081, set up credentials
    Go to Manage Jenkins → Tools → Allure Commandline installations and choose here Add Allure Commandline
    Go to plugins, install Allure Jenkins Plugin
    Create a Pipeline:
    Source: GitHub repository, e.g., https://github.com/VolhaMch/inno_task_relax.git

4. Launch pipeline in Jenkins
   