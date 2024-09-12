# import pytest
# from flask import Flask, jsonify
# from app import create_app


# # fixture, configurado para proporcionar un cliente de prueba para las solicitudes HTTP.
# @pytest.fixture
# def client():
#     app = create_app()
#     app.testing = True
#     # Usar test_client para obtener un cliente de prueba
#     with app.test_client() as client:
#         yield client


# def test_get_trajectories_success(client, monkeypatch):

#     # mock fetch_trajectories
#     def mock_fetch_trajectories(taxi_id, date_initial, date_end):
#         if taxi_id != "7088":  # Simula que solo el taxi_id "1234" tiene datos
#             return [], 404
#         return [
#             {
#                 "date": "Sat, 02 Feb 2008 14:36:10 GMT",
#                 "id": 8521,
#                 "latitude": 116.44724,
#                 "longitude": 39.89008,
#                 "taxiId": 7088,
#             },
#             {
#                 "date": "Sat, 02 Feb 2008 14:39:26 GMT",
#                 "id": 8522,
#                 "latitude": 116.44964,
#                 "longitude": 39.88968,
#                 "taxiId": 7088,
#             },
#             {
#                 "date": "Sat, 02 Feb 2008 14:41:36 GMT",
#                 "id": 8523,
#                 "latitude": 116.44951,
#                 "longitude": 39.89012,
#                 "taxiId": 7088,
#             },
#         ], 200

#     # Usar monkeypatch para reemplazar fetch_taxis con mock_fetch_taxis, se apunta al lugar
#     # donde esta siendo llamada la funcion
#     monkeypatch.setattr(
#         "app.controllers.trajectory_controller.fetch_trajectories",
#         mock_fetch_trajectories,
#     )

#     response = client.get("/trajectories?taxiId=7088&date=02-02-2008")
#     assert response.status_code == 200
#     assert response.json == [
#         {
#             "date": "Sat, 02 Feb 2008 14:36:10 GMT",
#             "id": 8521,
#             "latitude": 116.44724,
#             "longitude": 39.89008,
#             "taxiId": 7088,
#         },
#         {
#             "date": "Sat, 02 Feb 2008 14:39:26 GMT",
#             "id": 8522,
#             "latitude": 116.44964,
#             "longitude": 39.88968,
#             "taxiId": 7088,
#         },
#         {
#             "date": "Sat, 02 Feb 2008 14:41:36 GMT",
#             "id": 8523,
#             "latitude": 116.44951,
#             "longitude": 39.89012,
#             "taxiId": 7088,
#         },
#     ]


# def test_get_trajectories_missing_params(client, monkeypatch):
#     def mock_get_query_params_trajectories():
#         return None, None

#     monkeypatch.setattr(
#         "app.controllers.trajectory_controller.get_query_params_trajectories",
#         mock_get_query_params_trajectories,
#     )

#     response = client.get("/trajectories")
#     assert response.status_code == 400
#     assert response.json == {"error": "taxi_id and date are required"}


# def test_get_trajectories_invalid_date(client, monkeypatch):
#     def mock_get_query_params_trajectories():
#         return "1234", "02-02-22"

#     monkeypatch.setattr(
#         "app.controllers.trajectory_controller.get_query_params_trajectories",
#         mock_get_query_params_trajectories,
#     )

#     response = client.get("/trajectories?taxi_id=1234&date=02-02-22")
#     assert response.status_code == 400
#     assert response.json == {"error": "Date must be in 'dd-mm-yyyy' format."}


# def test_get_trajectories_exception(client, monkeypatch):
#     def mock_get_query_params_trajectories():
#         return "3456", "02-02-2028"

#     monkeypatch.setattr(
#         "app.controllers.trajectory_controller.get_query_params_trajectories",
#         mock_get_query_params_trajectories,
#     )

#     def mock_fetch_trajectories(taxi_id, date_initial_str, date_end_str):
#         raise Exception("Unexpected error")

#     monkeypatch.setattr(
#         "app.controllers.trajectory_controller.fetch_trajectories",
#         mock_fetch_trajectories,
#     )

#     response = client.get("/trajectories?taxi_id=3456&date=02-02-2028")
#     assert response.status_code == 500
#     assert response.json == {"Error": "Unexpected error"}
