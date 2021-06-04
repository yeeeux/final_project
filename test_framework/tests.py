
def test_status_user(client):
    response = client()
    response.raise_for_status()


def test_status_department(client):
    response = client(endpoint="departments")
    response.raise_for_status()


def test_random_user(random_user_data, client):
    user = random_user_data
    response = client(user)
    assert response.json() == user.split()
