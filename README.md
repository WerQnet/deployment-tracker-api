# Deployment Tracker API

A simple HTTP service for tracking application deployments across development, staging, and production environments.

## Features

- Health check endpoint
- Create deployment records
- List deployments
- Get the latest deployment for a service and environment
- Automated tests

## Run the service

Install dependencies:

```bash
python -m pip install -r requirements.txt

## Project purpose

This project is designed as a simple DevOps-oriented service that can later be containerized, tested in CI/CD pipelines, and deployed to Kubernetes.