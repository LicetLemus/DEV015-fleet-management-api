import pytest
from unittest.mock import MagicMock
from app.services.trajectory_service import fetch_trajectories
from app.models.trajectories import Trajectories


# Test data: List of trajectories objects to simulate query results
trajectories_data = [
    Trajectories(
        taxi_id=8935,
        date="Sat Feb 02 2008 13:37:40",
        latitude=116.45367,
        longitude=115.72647,
    ),
    Trajectories(
        taxi_id=8935,
        date="Sat Feb 02 2008 12:37:40",
        latitude=117.45367,
        longitude=118.72647,
    ),
    Trajectories(
        taxi_id=8935,
        date="Sat Feb 02 2008 16:37:40",
        latitude=119.45367,
        longitude=120.72647,
    ),
]


@pytest.fixture
def mock_session(mocker):
    """
    Fixture to create a mock SQLAlchemy session.
    """
    # Create a mock for the SQLAlchemy session
    session = mocker.MagicMock()

    # Create a mock for the query object
    query_mock = mocker.MagicMock()

    # Configure the mock so that the `all` method returns `taxis_data`
    query_mock.all.return_value = trajectories_data

    # Configure the session mock to return `query_mock` when `query` is called
    session.query.return_value = query_mock

    # Configure `filter` to return the same `query_mock`
    session.query.return_value.filter.return_value = query_mock

    # Return the mock session
    return session


def test_fetch_trajectories_invalid_filter(mocker, mock_session):

    mock_session.query.return_value.filter.return_value.all.return_value = []

    mocker.patch(
        "app.services.trajectory_service.get_session", return_value=mock_session
    )

    response, status_code = fetch_trajectories(
        2345, "02 02 2008 00:00:00", "02 02 2008 23:59:59"
    )

    assert status_code == 404
    assert response == {"error": "No trajectories found."}


def test_fetch_trajectories_parameters(mocker, mock_session):

    mock_session.query.return_value.filter.return_value.all.return_value = (
        trajectories_data
    )

    mocker.patch(
        "app.services.trajectory_service.get_session", return_value=mock_session
    )

    response, status_code = fetch_trajectories(
        8935, "02 02 2008 00:00:00", "02 02 2008 23:59:59"
    )

    assert status_code == 200
    assert response[0]["date"] == "Sat Feb 02 2008 13:37:40"
    assert response[1]["date"] == "Sat Feb 02 2008 12:37:40"
