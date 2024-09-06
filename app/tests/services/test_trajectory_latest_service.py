import pytest
from unittest.mock import MagicMock
from app.services.trajectory_latest_service import fetch_trajectory_latest
from sqlalchemy.orm import Query


@pytest.fixture
def mock_session(mocker):
    """
    Fixture para crear una sesión SQLAlchemy mock.
    """
    session = mocker.MagicMock()
    query_mock = mocker.MagicMock(spec=Query)
    subquery_mock = mocker.MagicMock()

    # Mockear el subquery para devolver datos mock
    subquery_mock.c.taxi_id = "taxi_id"
    subquery_mock.c.latest_date = "latest_date"
    session.query.return_value.subquery.return_value = subquery_mock

    return session


def test_fetch_trajectory_latest_with_results(mocker, mock_session):
    taxi = MagicMock()
    taxi.plate = "XYZ-1234"

    trajectory1 = MagicMock(
        id=1,
        taxi_id=8935,
        date="Sat Feb 02 2008 16:37:40",
        latitude=119.45367,
        longitude=120.72647,
        plate=taxi.plate,
    )

    trajectory2 = MagicMock(
        id=2,
        taxi_id=8935,
        date="Sat Feb 02 2008 12:37:40",
        latitude=117.45367,
        longitude=118.72647,
        plate=taxi.plate,
    )

    trajectory3 = MagicMock(
        id=3,
        taxi_id=8935,
        date="Sat Feb 02 2008 13:37:40",
        latitude=116.45367,
        longitude=115.72647,
        plate=taxi.plate,
    )

    # Mockear la sesión para devolver la lista completa de trayectorias
    mock_session.query.return_value.join.return_value.join.return_value.distinct.return_value.all.return_value = [
        trajectory1
    ]

    # Simular la función get_session para devolver la sesión mock
    mocker.patch(
        "app.services.trajectory_latest_service.get_session", return_value=mock_session
    )

    # Llamar a la función y obtener la respuesta
    response, status_code = fetch_trajectory_latest()

    # Verificar el estado y la respuesta
    assert status_code == 200
    assert response["total_trajectories"] == 1
    assert response["trajectories"][0]["date"] == "Sat Feb 02 2008 16:37:40"
    assert response["trajectories"][0]["plate"] == "XYZ-1234"


def test_fetch_trajectory_latest_with_exception(mocker, mock_session):
    """
    Prueba que verifica el comportamiento de `fetch_trajectory_latest` cuando ocurre una excepción.
    """
    # Configurar el mock para lanzar una excepción
    mock_session.query.side_effect = Exception("Database error")
    mocker.patch(
        "app.services.trajectory_latest_service.get_session", return_value=mock_session
    )

    response, status_code = fetch_trajectory_latest()

    assert status_code == 500
    assert response["error"] == "Database error"
