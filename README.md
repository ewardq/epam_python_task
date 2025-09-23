# Automated CI/CD System with SonarQube, GitHub Actions, and AWS Deployment

This project implements a fully automated DevSecOps pipeline for Python packages, integrating code quality, security, and deployment workflows. The system:

- Runs unit tests for multiple Python packages within GitHub Actions.
- Performs static code analysis and security scans using SonarQube and security agents (hosted in AWS).
- Enforces compliance by automatically merging code only if quality gates and coverage thresholds are met.
- Updates the project README with latest test coverage and reports, pulling information from both SonarQube and GitHub Releases.
- Builds Docker images and publishes them to GitHub Container Registry.
- Deploys validated artifacts to AWS infrastructure.

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
<img src="./repo_images/SonarQube.svg">

### Publish Docker image to Docker Hub
<img src="./repo_images/DockerHub.svg">

### Publish Docker image to GitHub packages
<img src="./repo_images/GitHub_packages.svg">

### Run Python unit tests
<img src="./repo_images/GitHub_unit_tests.svg">
