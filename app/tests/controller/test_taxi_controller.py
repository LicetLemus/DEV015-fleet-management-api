# import pytest
# from flask import Flask, jsonify
# from app import create_app


# # fixture, configurado para proporcionar un cliente de prueba para las solicitudes HTTP.


# @pytest.fixture  # Configurar el entorno de prueba y proporcionar datos o recursos necesarios.
# def client():
#     app = create_app()  # configura la aplicación Flask
#     app.testing = (
#         True  # Proporciona un cliente para realizar solicitudes HTTP a la aplicación
#     )
#     with app.test_client() as client:
#         yield client  # El cliente está disponible para las pruebas hasta que se complete el test.


# def test_get_taxis_all(client, monkeypatch):
#     # Mock para la función fetch_taxis

#     def mock_fetch_taxis(plate, page, limit):
#         return [{
#             "id": 7249, 
#             "plate": "CNCJ-2997"
#         },
#         {
#             "id": 10133,
#             "plate": "PAOF-6727"
#         }], 200

#     # Usar monkeypatch para reemplazar fetch_taxis con mock_fetch_taxis, se apunta al lugar
#     # donde esta siendo llamada la funcion
#     monkeypatch.setattr("app.controllers.taxi_controller.fetch_taxis", mock_fetch_taxis)

#     response = client.get("/taxis")
#     assert response.status_code == 200
#     assert response.json == [{
#             "id": 7249, 
#             "plate": "CNCJ-2997"
#         },
#         {
#             "id": 10133,
#             "plate": "PAOF-6727"
#         }]


# def test_get_taxis_by_plate(client, monkeypatch):
#     # Mock para la función fetch_taxis

#     def mock_fetch_taxis(plate, page, limit):
#         return [
#                 {"id": 2, "plate": "CNCJ-2997"},
#             ], 200

#     # Usar monkeypatch para reemplazar fetch_taxis con mock_fetch_taxis, se apunta al lugar
#     # donde esta siendo llamada la funcion
#     monkeypatch.setattr("app.controllers.taxi_controller.fetch_taxis", mock_fetch_taxis)

#     response = client.get("/taxis?plate=CNCJ-2997")
#     assert response.status_code == 200
#     assert response.json == [
#                 {"id": 2, "plate": "CNCJ-2997"},
#             ]


# def test_get_taxis_invalid_parameters(client):
#     response = client.get("/taxis?page=-1&limit=10")
#     assert response.status_code == 400
#     assert response.json == {"error": "Page number and limit must be greater than 0."}


# def test_get_taxis_invalid_plate(client, monkeypatch):
#     def mock_fetch_taxis(plate, page, limit):
#         return {"error": "No taxis found."}, 404

#     monkeypatch.setattr("app.controllers.taxi_controller.fetch_taxis", mock_fetch_taxis)

#     response = client.get("/taxis?plate=345-")
#     assert response.status_code == 404
#     assert response.json == {"error": "No taxis found."}
