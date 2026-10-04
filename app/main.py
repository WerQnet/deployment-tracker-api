import os
from flask import Flask, jsonify, request


app = Flask(__name__)

deployments = []


@app.get("/healthz")
def healthz():
    return jsonify({
        "status": "ok"
    }), 200


@app.get("/deployments")
def get_deployments():
    return jsonify(deployments), 200


@app.post("/deployments")
def create_deployment():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "JSON body is required"
        }), 400

    required_fields = ["service", "version", "environment"]

    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    deployment = {
        "service": data["service"],
        "version": data["version"],
        "environment": data["environment"]
    }

    deployments.append(deployment)

    return jsonify(deployment), 201


@app.get("/deployments/latest")
def latest_deployment():
    service = request.args.get("service")
    environment = request.args.get("environment")

    if not service or not environment:
        return jsonify({
            "error": "service and environment are required"
        }), 400

    matches = [
        deployment
        for deployment in deployments
        if deployment["service"] == service
        and deployment["environment"] == environment
    ]

    if not matches:
        return jsonify({
            "error": "deployment not found"
        }), 404

    return jsonify(matches[-1]), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))

    app.run(
        host="0.0.0.0",
        port=port
    )