# Automated CI/CD System with SonarQube, GitHub Actions, and AWS Deployment.

This project implements a fully automated DevSecOps pipeline for Python packages, integrating code quality, security, and deployment workflows. The system:

- Runs unit tests for multiple Python packages within GitHub Actions.
- Performs static code analysis and security scans using SonarQube and security agents (hosted in AWS).
- Enforces compliance by automatically merging code only if quality gates and coverage thresholds are met.
- Updates the project README with latest test coverage and reports, pulling information from both SonarQube and GitHub Releases.
- Builds Docker images and publishes them to GitHub Container Registry.
- Deploys validated artifacts to AWS infrastructure.

<img src="./repo_images/Complete_CICD.svg">


## SonarQube report
<div align="center">

|Current code status |[![Quality gate](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/quality_gate.svg)](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/quality_gate.svg) |
|---	|---	|

|Current Status |Acceptance Condition|   
|---	|---	|
|[![Security Issues](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/software_quality_security_issues.svg)](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/software_quality_security_issues.svg) |New code has 0 security issues|
|[![Reliability Issues](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/software_quality_reliability_issues.svg)](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/software_quality_reliability_issues.svg) |New code has 0 reliability issues |
|[![Coverage](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/coverage.svg)](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/coverage.svg) |New code has at least 80% coverage |
|[![Duplicated Lines (%)](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/duplicated_lines_density.svg)](https://github.com/ewardq/epam_python_task/blob/master/repo_images/sonarqube_badges/duplicated_lines_density.svg) |Code has less than 3% of lines duplicated |

</div>

## GitHub Actions breakdown

### SonarQube analysis
[![SonarQube analysis](https://github.com/ewardq/epam_python_task/actions/workflows/sonarqube.yml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/sonarqube.yml)

<img src="./repo_images/SonarQube.svg">


### Update SonarQube analysis results badges  
[![Update SonarQube Badges](https://github.com/ewardq/epam_python_task/actions/workflows/create_sonar_badges.yaml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/create_sonar_badges.yaml)

<img src="./repo_images/Update_SonarQube_badges.svg">


### Publish Docker image to Docker Hub
[![Publish Docker image](https://github.com/ewardq/epam_python_task/actions/workflows/push_to_docker_hub.yaml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/push_to_docker_hub.yaml)

<img src="./repo_images/DockerHub.svg">


### Publish Docker image to GitHub packages
[![Create and publish a Docker image](https://github.com/ewardq/epam_python_task/actions/workflows/build_and_push_registry.yaml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/build_and_push_registry.yaml)

<img src="./repo_images/GitHub_packages.svg">


### Run Python unit tests
[![Run Python Unit Test](https://github.com/ewardq/epam_python_task/actions/workflows/execute_pytests.yml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/execute_pytests.yml)

<img src="./repo_images/GitHub_unit_tests.svg">


### Deploy in AWS Elastic Container Service
[![Deploy to Amazon ECS](https://github.com/ewardq/epam_python_task/actions/workflows/deploy_in_aws.yml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/deploy_in_aws.yml)

<img src="./repo_images/Deploy_to_ECS.svg">
