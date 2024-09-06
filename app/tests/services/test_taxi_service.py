import pytest
from unittest.mock import MagicMock
from app.services.taxi_service import fetch_taxis
from app.models.taxis import Taxis


# Test data: List of Taxis objects to simulate query results
taxis_data = [
    Taxis(id=7956, plate="CCKF-1601"),
    Taxis(id=252, plate="LAHG-7611"),
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
    query_mock.all.return_value = taxis_data

    # Configure the session mock to return `query_mock` when `query` is called
    session.query.return_value = query_mock

    # Configure `filter` to return the same `query_mock`
    session.query.return_value.filter.return_value = query_mock

    # Configure `offset` to return the same `query_mock`
    session.query.return_value.offset.return_value = session.query.return_value

    # Configure `limit` to return the same `query_mock`
    session.query.return_value.limit.return_value = session.query.return_value

    # Return the mock session
    return session


def test_fetch_taxis_no_filter(mocker, mock_session):
    """
    Test that verifies the behavior of `fetch_taxis` without applying filters.
    """

    # Mock `get_session` to return `mock_session`
    mocker.patch("app.services.taxi_service.get_session", return_value=mock_session)

    # Call the `fetch_taxis` function without a filter
    response, status_code = fetch_taxis(None, 0, 0)

    assert status_code == 200
    assert response["total_results"] == 2
    assert response["taxis"][0]["plate"] == "CCKF-1601"
    assert response["taxis"][1]["plate"] == "LAHG-7611"


def test_fetch_taxis_with_filter(mocker, mock_session):
    # Configure mock return only taxi
    mock_session.query.return_value.filter.return_value.all.return_value = [
        Taxis(id=7956, plate="CCKF-1601")
    ]
    # Mock `get_session` to return `mock_session`
    mocker.patch("app.services.taxi_service.get_session", return_value=mock_session)

    response, status_code = fetch_taxis("CCKF-1601", 1, 10)

    assert status_code == 200
    assert response["total_results"] == 1
    assert len(response["taxis"]) == 1
    assert response["taxis"][0]["plate"] == "CCKF-1601"


def test_fetch_taxis_no_results(mocker, mock_session):
    # Mock `get_session` to return `mock_session`

    mock_session.query.return_value.filter.return_value.all.return_value = []
    mocker.patch("app.services.taxi_service.get_session", return_value=mock_session)

    response, status_code = fetch_taxis("ADF-7654", 1, 10)

    assert status_code == 404
    assert response["error"] == "No taxis found."
