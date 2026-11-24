# Deployment Tracker API

Deployment Tracker API is a simple HTTP service for recording application deployments and checking which version of a service is deployed in development, staging, or production environments.

## What it does

The service stores information about application deployments.

Each deployment record contains:
- service name
- application version
- environment

Example deployment record:

```json
{
  "service": "shop-api",
  "version": "v1.0.0",
  "environment": "production"
}
```

## Run

Install the required dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Start the service:

```bash
./scripts/run.sh
```

## PORT

The service listens on PORT 8080 by default.

The PORT can be changed using the PORT environment variable.

Example:

```bash
PORT=5000 ./scripts/run.sh
```

The service will then be available at:

```text
http://localhost:5000
```

## Health Check

The service provides a health check endpoint:

```text
GET /healthz
```

Test it with:

```bash
curl http://localhost:8080/healthz
```

Expected response:

```json
{
  "status": "ok"
}
```

The health check returns HTTP status 200.

## API Endpoints

### GET /

Returns basic information about the service.

Example:

```bash
curl http://localhost:8080/
```

Expected response:

```json
{
  "service": "Deployment Tracker API",
  "status": "running"
}
```

### GET /healthz

Checks whether the application is running.

Example:

```bash
curl http://localhost:8080/healthz
```

### POST /deployments

Creates a new deployment record.

Example:

```bash
curl -X POST http://localhost:8080/deployments -H "Content-Type: application/json" -d "{\"service\":\"shop-api\",\"version\":\"v1.0.0\",\"environment\":\"production\"}"
```

### GET /deployments

Returns all deployment records.

Example:

```bash
curl http://localhost:8080/deployments
```

### GET /deployments/latest

Returns the latest deployment for a specific service and environment.

Example:

```bash
curl "http://localhost:8080/deployments/latest?service=shop-api&environment=production"
```

## Testing

Run the automated tests with:

```bash
./scripts/test.sh
```

Expected output:

```text
TESTS: 4/4
```

The project contains four automated tests.

The tests check:
- the health check endpoint
- creation of a deployment
- retrieval of the latest deployment
- validation of missing required fields

## Project Structure

```text
deployment-tracker-api/
├── app/
│   ├── __init__.py
│   └── main.py
├── scripts/
│   ├── run.sh
│   └── test.sh
├── tests/
│   └── test_api.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Rollback

Argo CD deploys the `main` branch from the `k8s` folder into the default namespace. Automatic sync, pruning and self-healing keep the deployment aligned with Git. CI builds and publishes images, but does not deploy to the cluster.

To roll back a bad image, find the commit that changed the image and revert it:

```bash
git switch main
git pull --ff-only
git log --oneline -- k8s/deployment.yaml
git revert <image-bump-commit>
git push origin main
```

If reverting a merge commit, use `git revert -m 1 <merge-commit>` instead. Argo CD reconciles to the previous image within about three minutes. Do not use `kubectl rollout undo`: self-heal would restore the version declared in Git. The `app-secret` is created outside Git and is not managed by Argo CD.
