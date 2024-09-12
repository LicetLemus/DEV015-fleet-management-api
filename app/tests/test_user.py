import pytest
import json
from app.models.users import Users


def test_example(test_client):
    # Usa `test_client` para hacer solicitudes a tu API
    response = test_client.get("/")
    assert response.status_code == 200
    assert '¡Hola, mundo!' in response.data.decode('utf-8')


def test_create_user_in_db(test_client):
    data_user = {
        "name": "Carla Martin",
        "email": "carla@example.com",
        "password": "key132345"
    }

    response = test_client.post('/users', json=data_user)
    assert response.status_code == 201
    response_json = response.json
    
    # Verifica la respuesta JSON
    assert response_json['name'] == "Carla Martin"
    assert response_json['email'] == "carla@example.com"
    
    # Consulta la base de datos para verificar que el usuario fue creado
    created_user = Users.query.filter_by(email="carla@example.com").first()
    assert created_user is not None
    assert created_user.name == "Carla Martin"



def test_fetch_users_from_db(test_client):
    # Primero, asegúrate de que la base de datos tiene el estado esperado
    # Puedes agregar un usuario de prueba aquí si es necesario

    response = test_client.get('/users')
    assert response.status_code == 200
    users = response.json
    
    # Verifica que la respuesta tenga la estructura esperada
    assert isinstance(users, list)
    assert len(users) > 0  # O el número esperado de usuarios

    # Verifica un usuario específico
    user_names = [user['name'] for user in users]
    assert "Carla Martin" in user_names
    

def test_update_user_in_db(test_client):
    data_user = {
        "name": "Carla Martin",
        "email": "grace@example.com",
        "password": "key132345"
    }
    
    response = test_client.patch('/users/1', json=data_user)
    assert response.status_code == 400
    assert response.json['error'] == "fields can not be updated"
    

def test_update_user_in_db_name(test_client):
    data_user = {
        "name": "Carla Martin Updated",
    }
    
    response = test_client.patch('/users/1', json=data_user)
    assert response.status_code == 200
    response_json = json.loads(response.data)
    
    # Verifica la respuesta JSON
    assert response_json['name'] == "Carla Martin Updated"
    assert response_json['email'] == "carla@example.com"

    # Consulta la base de datos para verificar el cambio
    updated_user = Users.query.get(1)
    assert updated_user is not None
    assert updated_user.name == "Carla Martin Updated"
    assert updated_user.email == "carla@example.com"