import pytest
from app.models.trajectories import Trajectories

def test_fetch_trajectory_latest_success(test_client):

    response = test_client.get("/trajectories/latest")

    assert response.status_code == 200
    data = response.get_json()
    
    assert (
        trajectory["taxiId"] == 1 and trajectory["date"] == "Sat Feb 08 2008 12:37:40"
        for trajectory in data
    )
