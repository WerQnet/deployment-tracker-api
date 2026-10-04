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
