# import pytest
# from unittest.mock import MagicMock
# from app.services.trajectory_latest_service import fetch_trajectory_latest
# from sqlalchemy.orm import Query


# @pytest.fixture
# def mock_session(mocker):
#     mock = mocker.Mock()
#     return mock


# def test_fetch_trajectory_latest_success(mocker, mock_session):
#     # Crear datos de prueba
#     trajectory = MagicMock(
#         id=8935,
#         latitude=117.45367,
#         longitude=118.72647,
#         plate="XYZ-1234",
#         date="Sat Feb 08 2008 12:37:40",
#     )

#     # Configurar el mock de la sesión para devolver datos de prueba
#     mock_session.query.return_value.join.return_value.join.return_value.distinct.return_value.all.return_value = [
#         trajectory
#     ]

#     # Configurar el mock de get_session
#     mocker.patch(
#         "app.services.trajectory_latest_service.get_session", return_value=mock_session
#     )
#     mocker.patch("app.services.trajectory_latest_service.validation_session")

#     # Llamar a la función
#     response, status_code = fetch_trajectory_latest()

#     # Verificar los resultados
#     assert status_code == 200
#     assert response[0]["taxiId"] == 8935
#     assert response[0]["latitude"] == 117.45367
#     assert response[0]["longitude"] == 118.72647
#     assert response[0]["plate"] == "XYZ-1234"
#     assert response[0]["timestamp"] == "Sat Feb 08 2008 12:37:40"


# def test_fetch_trajectory_latest_no_results(mocker, mock_session):
#     # Configurar el mock de la sesión para devolver una lista vacía
#     mock_session.query.return_value.join.return_value.join.return_value.distinct.return_value.all.return_value = (
#         []
#     )

#     # Configurar el mock de get_session
#     mocker.patch(
#         "app.services.trajectory_latest_service.get_session", return_value=mock_session
#     )
#     mocker.patch("app.services.trajectory_latest_service.validation_session")

#     # Llamar a la función
#     response, status_code = fetch_trajectory_latest()

#     # Verificar los resultados
#     assert status_code == 404
#     assert response["error"] == "No trajectories found."


# def test_fetch_trajectory_latest_with_exception(mocker, mock_session):
#     """
#     Prueba que verifica el comportamiento de `fetch_trajectory_latest` cuando ocurre una excepción.
#     """
#     # Configurar el mock para lanzar una excepción
#     mock_session.query.side_effect = Exception("Database error")
#     mocker.patch(
#         "app.services.trajectory_latest_service.get_session", return_value=mock_session
#     )

#     response, status_code = fetch_trajectory_latest()

#     assert status_code == 500
#     assert response["error"] == "Database error"


# def test_fetch_trajectory_latest_session_closes(mocker, mock_session):
#     # Crear datos de prueba
#     trajectory = MagicMock(
#         id=8935,
#         latitude=117.45367,
#         longitude=118.72647,
#         plate="XYZ-1234",
#         date="Sat Feb 08 2008 12:37:40",
#     )

#     # Configurar el mock de la sesión para devolver datos de prueba
#     mock_session.query.return_value.join.return_value.join.return_value.distinct.return_value.all.return_value = [
#         trajectory
#     ]

#     # Configurar el mock de get_session
#     mocker.patch(
#         "app.services.trajectory_latest_service.get_session", return_value=mock_session
#     )
#     mocker.patch("app.services.trajectory_latest_service.validation_session")

#     # Llamar a la función
#     fetch_trajectory_latest()

#     # Verificar que la sesión se cierra
#     mock_session.close.assert_called_once()
