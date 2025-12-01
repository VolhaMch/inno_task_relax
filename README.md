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

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --user root \
  jenkins/jenkins:lts
