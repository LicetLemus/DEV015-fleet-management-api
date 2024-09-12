import pytest
from app.models.taxis import Taxis



def test_fetch_taxis_success(test_client):
    response = test_client.get("/taxis?page=1&limit=3")
    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "plate": "CCKF-1601"},
        {"id": 2, "plate": "SDFE-6754"}
    ]
    
    taxi = Taxis.query.filter_by(plate="CCKF-1601").first()
    assert taxi is not None
    assert taxi.id == 1


def test_fetch_taxis_no_results(test_client):
    response = test_client.get("/taxis?plate=SDFR-1234")
    assert response.status_code == 404
    assert response.json == {"error": "No taxis found."}

