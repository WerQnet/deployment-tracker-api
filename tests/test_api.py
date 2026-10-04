from app.main import app, deployments


def setup_function():
    deployments.clear()


def test_healthz():
    client = app.test_client()

    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_create_deployment():
    client = app.test_client()

    response = client.post(
        "/deployments",
        json={
            "service": "shop-api",
            "version": "v1.0.0",
            "environment": "production"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["service"] == "shop-api"
    assert data["version"] == "v1.0.0"
    assert data["environment"] == "production"


def test_latest_deployment():
    client = app.test_client()

    client.post(
        "/deployments",
        json={
            "service": "shop-api",
            "version": "v1.0.0",
            "environment": "production"
        }
    )

    client.post(
        "/deployments",
        json={
            "service": "shop-api",
            "version": "v1.1.0",
            "environment": "production"
        }
    )

    response = client.get(
        "/deployments/latest?service=shop-api&environment=production"
    )

    assert response.status_code == 200
    assert response.get_json()["version"] == "v1.1.0"


def test_missing_fields():
    client = app.test_client()

    response = client.post(
        "/deployments",
        json={
            "service": "shop-api"
        }
    )

    assert response.status_code == 400