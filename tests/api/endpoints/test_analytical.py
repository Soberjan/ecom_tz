from fastapi.testclient import TestClient
from tests.database.database_fixture import database, filled_db 
from client_fixture import client 

def test_analytical(client: TestClient):
    data = client.get("/students/more-than-3-twos").json()
    assert data['result'][0]["full_name"] == 'Вася'
    assert data['result'][0]["count_twos"] == 4

    data = client.get("/students/less-than-5-twos").json()
    assert data['result'][0]["full_name"] == 'Вася'
    assert data['result'][0]["count_twos"] == 4
