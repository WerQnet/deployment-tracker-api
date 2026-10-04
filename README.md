# Deployment Tracker API

A simple HTTP service for tracking application deployments across development, staging, and production environments.

## Features

- Health check endpoint
- Create deployment records
- List deployments
- Get the latest deployment for a service and environment
- Automated tests


## Project purpose

This project is designed as a simple DevOps-oriented service that can later be containerized, tested in CI/CD pipelines, and deployed to Kubernetes.

## What it does

Deployment Tracker API is an HTTP service for recording application deployments and checking deployed versions across development, staging, and production environments.

## Run

Install dependencies:

```bash
python3 -m pip install -r requirements.txt