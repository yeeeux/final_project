import users
import pytest
import requests
from users import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_square(client):
    rv = client.get("/users?nusername=pe")
    print(rv.json)
    assert rv.json == 1

