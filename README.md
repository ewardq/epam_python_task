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
This project aims to automate as much as possible of the CI/CD pipeline git GitHub actions, so each time there is a commit to the master branch, all workflows (except release to docker hub and GitHub packages) run.
<div align="center">
<img width="897" height="435" alt="image" src="https://github.com/user-attachments/assets/4015dca2-4fb6-48dd-bddf-4277c5ae8e84" />
</div>

### SonarQube analysis
[![SonarQube analysis](https://github.com/ewardq/epam_python_task/actions/workflows/sonarqube.yml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/sonarqube.yml)

<img src="./repo_images/SonarQube.svg">

|Workflow output |SonarQube platform |
|---	|---	|
|<img width="1355" height="363" alt="image" src="https://github.com/user-attachments/assets/92b53126-3093-4b47-823a-b02e3feae6c9" /> |<img width="1353" height="241" alt="image" src="https://github.com/user-attachments/assets/027bb34a-c9e8-4c6e-96ab-70585f05d17b" /> |


### Update SonarQube analysis results badges  
[![Update SonarQube Badges](https://github.com/ewardq/epam_python_task/actions/workflows/create_sonar_badges.yaml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/create_sonar_badges.yaml)

<div align="center">
<img src="./repo_images/Update_SonarQube_badges.svg">
</div>

|Workflow output |Images on repo |
|---	|---	|
|<img width="999" height="337" alt="image" src="https://github.com/user-attachments/assets/9d086dcc-2dfb-4d23-8415-a725bed2c03a" /> |<img width="995" height="665" alt="image" src="https://github.com/user-attachments/assets/7c0d6c8f-d775-4696-9493-169055e62b14" /> |

### Publish Docker image to Docker Hub
[![Publish Docker image](https://github.com/ewardq/epam_python_task/actions/workflows/push_to_docker_hub.yaml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/push_to_docker_hub.yaml)

<div align="center">
<img src="./repo_images/DockerHub.svg">
</div>

|Workflow output |Package on repo |
|---	|---	|
|<img width="992" height="823" alt="image" src="https://github.com/user-attachments/assets/835ff36c-a6a0-4c18-8618-da8cda35c0f8" /> |<img width="908" height="613" alt="image" src="https://github.com/user-attachments/assets/841e3c09-c8d5-4353-b08e-56f303e9acc2" /> |

### Publish Docker image to GitHub packages
[![Create and publish a Docker image](https://github.com/ewardq/epam_python_task/actions/workflows/build_and_push_registry.yaml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/build_and_push_registry.yaml)

<div align="center">
<img src="./repo_images/GitHub_packages.svg">
</div>


### Run Python unit tests
[![Run Python Unit Test](https://github.com/ewardq/epam_python_task/actions/workflows/execute_pytests.yml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/execute_pytests.yml)

<div align="center">
<img src="./repo_images/GitHub_unit_tests.svg">
</div>

|Workflow output |Coverage report |
|---	|---	|
|<img width="1001" height="755" alt="image" src="https://github.com/user-attachments/assets/1af00d14-878b-445e-b246-49c53c85ce9c" /> |<img width="928" height="894" alt="image" src="https://github.com/user-attachments/assets/914b7b1f-68c3-4e1e-a6d5-728a52b3d460" /> |

### Deploy in AWS Elastic Container Service
[![Deploy to Amazon ECS](https://github.com/ewardq/epam_python_task/actions/workflows/deploy_in_aws.yml/badge.svg)](https://github.com/ewardq/epam_python_task/actions/workflows/deploy_in_aws.yml)

<div align="center">
<img src="./repo_images/Deploy_to_ECS.svg">
</div>

|Load Balancer |ECR images |
|---	|---	|
|<img width="1587" height="488" alt="image" src="https://github.com/user-attachments/assets/00810da5-3b9e-410a-882a-2aa840a907ea" /> |<img width="1897" height="684" alt="image" src="https://github.com/user-attachments/assets/d244df5f-243f-4777-ac11-11a74072cd00" /> |


|ECS Cluster |
|---	|
|<img width="1896" height="712" alt="image" src="https://github.com/user-attachments/assets/f79c9394-0c1c-4b56-9044-fd968fa26cb4" /> |
