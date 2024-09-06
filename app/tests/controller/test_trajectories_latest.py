import pytest
from flask import Flask, jsonify
from app import create_app


@pytest.fixture  # Configurar el entorno de prueba y proporcionar datos o recursos necesarios.
def client():
    app = create_app()  # configura la aplicación Flask
    app.testing = (
        True  # Proporciona un cliente para realizar solicitudes HTTP a la aplicación
    )
    with app.test_client() as client:
        yield client


def test_get_trajectory_latest(client, monkeypatch):
    # mock fetch_trajectory_latest

    def mock_fetch_trajectory_latest():
        return {
            "total_trajectories": 2,
            "trajectories": [
                {
                    "date": "Fri, 08 Feb 2008 17:39:06 GMT",
                    "id": 9275,
                    "latitude": 116.1008,
                    "longitude": 39.95598,
                    "plate": "ENPB-7532",
                    "taxi_id": 9275,
                },
                {
                    "date": "Fri, 08 Feb 2008 16:07:16 GMT",
                    "id": 10133,
                    "latitude": 116.11806,
                    "longitude": 39.72814,
                    "plate": "PAOF-6727",
                    "taxi_id": 10133,
                },
            ],
        }, 200

    monkeypatch.setattr(
        "app.controllers.trajectory_latest.fetch_trajectory_latest",
        mock_fetch_trajectory_latest,
    )

    response = client.get("/trajectories/latest")

    assert response.status_code == 200
    assert response.json == {
        "total_trajectories": 2,
        "trajectories": [
            {
                "date": "Fri, 08 Feb 2008 17:39:06 GMT",
                "id": 9275,
                "latitude": 116.1008,
                "longitude": 39.95598,
                "plate": "ENPB-7532",
                "taxi_id": 9275,
            },
            {
                "date": "Fri, 08 Feb 2008 16:07:16 GMT",
                "id": 10133,
                "latitude": 116.11806,
                "longitude": 39.72814,
                "plate": "PAOF-6727",
                "taxi_id": 10133,
            },
        ],
    }


def test_get_trajectories_latest_exception(client, monkeypatch):
    # mock fetch_trajectory_latest

    def mock_fetch_trajectory_latest():
        raise Exception("Unexpected error")

    monkeypatch.setattr(
        "app.controllers.trajectory_latest.fetch_trajectory_latest",
        mock_fetch_trajectory_latest,
    )

    response = client.get("/trajectories/latest")
    assert response.status_code == 500
    assert response.json == {"error": "Unexpected error"}
