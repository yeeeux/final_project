
def test_status_user(client):
    response = client()
    response.raise_for_status()


def test_status_department(client):
    response = client(endpoint="departments")
    response.raise_for_status()


def test_random_user(random_user_data, client):
    response = client(random_user_data['username'])
    assert response.json()[0] == random_user_data
