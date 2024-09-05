import pytest
from flask import Flask, jsonify
from app import create_app
from app.services.trajectories_services import fetch_trajectories


# fixture, configurado para proporcionar un cliente de prueba para las solicitudes HTTP.
@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    # Usar test_client para obtener un cliente de prueba
    with app.test_client() as client:
        yield client


def test_get_trajectories_success(client, monkeypatch):

    # Mock para los parámetros de consulta (query params)
    def mock_get_query_params_trajectories():
        return "1234", "02-02-2022"

    monkeypatch.setattr(
        "app.controllers.trajectories_controller.get_query_params_trajectories",
        mock_get_query_params_trajectories,
    )

    # mock fetch_trajectories
    def mock_fetch_trajectories(taxi_id, date_initial, date_end):
        return {
            "total_trajectories": 2,
            "trajectories": [
                {
                    "id": 1,
                    "taxi_id": taxi_id,
                    "date": date_initial,
                    "latitude": 12.34,
                    "longitude": 56.78,
                },
                {
                    "id": 2,
                    "taxi_id": taxi_id,
                    "date": date_end,
                    "latitude": 12.34,
                    "longitude": 56.78,
                },
            ],
        }, 200

    # Usar monkeypatch para reemplazar fetch_taxis con mock_fetch_taxis, se apunta al lugar
    # donde esta siendo llamada la funcion
    monkeypatch.setattr(
        "app.controllers.trajectories_controller.fetch_trajectories",
        mock_fetch_trajectories,
    )

    response = client.get("/trajectories?taxi_id=1234&date=02-02-2022")
    assert response.status_code == 200
    assert response.json == {
        "total_trajectories": 2,
        "trajectories": [
            {
                "id": 1,
                "taxi_id": "1234",
                "date": "2022-02-02 00:00:00",
                "latitude": 12.34,
                "longitude": 56.78,
            },
            {
                "id": 2,
                "taxi_id": "1234",
                "date": "2022-02-02 23:59:59",
                "latitude": 12.34,
                "longitude": 56.78,
            },
        ],
    }


def test_get_trajectories_missing_params(client, monkeypatch):
    def mock_get_query_params_trajectories():
        return None, None

    monkeypatch.setattr(
        "app.controllers.trajectories_controller.get_query_params_trajectories",
        mock_get_query_params_trajectories,
    )

    response = client.get("/trajectories")
    assert response.status_code == 400
    assert response.json == {"error": "taxi_id and date are required"}


def test_get_trajectories_invalid_date(client, monkeypatch):
    def mock_get_query_params_trajectories():
        return "1234", "02-02-22"

    monkeypatch.setattr(
        "app.controllers.trajectories_controller.get_query_params_trajectories",
        mock_get_query_params_trajectories,
    )

    response = client.get("/trajectories?taxi_id=1234&date=02-02-22")
    assert response.status_code == 400
    assert response.json == {"error": "Date must be in 'dd-mm-yyyy' format."}


def test_get_trajectories_exception(client, monkeypatch):
    def mock_get_query_params_trajectories():
        return "3456", "02-02-2028"
    
    monkeypatch.setattr("app.controllers.trajectories_controller.get_query_params_trajectories", mock_get_query_params_trajectories)
    
    def mock_fetch_trajectories(taxi_id, date_initial_str, date_end_str):
        raise Exception("Unexpected error")
    
    monkeypatch.setattr("app.controllers.trajectories_controller.fetch_trajectories", mock_fetch_trajectories)
    
    response = client.get("/trajectories?taxi_id=3456&date=02-02-2028")
    assert response.status_code == 500
    assert response.json == {"Error": "Unexpected error"}