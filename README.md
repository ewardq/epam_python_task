# Automated CI/CD System with SonarQube, GitHub Actions, and AWS Deployment Sept 2025

This project implements a fully automated DevSecOps pipeline for Python packages, integrating code quality, security, and deployment workflows. The system:

- Runs unit tests for multiple Python packages within GitHub Actions.
- Performs static code analysis and security scans using SonarQube and security agents (hosted in AWS).
- Enforces compliance by automatically merging code only if quality gates and coverage thresholds are met.
- Updates the project README with latest test coverage and reports, pulling information from both SonarQube and GitHub Releases.
- Builds Docker images and publishes them to GitHub Container Registry.
- Deploys validated artifacts to AWS infrastructure.
