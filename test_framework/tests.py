
def test_status_user(client):
    response = client()
    assert response.status_code == 200


def test_status_department(depart_client):
    response = depart_client()
    assert response.status_code == 200

