import pytest
from app.models.trajectories import Trajectories


def test_fetch_trajectories_invalid_filter(test_client):

    response = test_client.get("/trajectories?taxiId=2&date=02-08-2008")

    assert response.status_code == 404
    assert response.json == {"error": "No trajectories found."}


def test_fetch_trajectories_parameters(test_client):
    response = test_client.get("/trajectories?taxiId=1&date=02-02-2008")

    assert response.status_code == 200
    
    data = response.get_json()

    assert any(
        trajectory['latitude'] == 117.45367 for trajectory in data
    )
