import pytest
from users import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_status_user(client):
    rv = client.get("/users")
    assert rv.status_code == 200


def test_status_user_with_filter(client):
    rv = client.get("/users?username=Pe")
    assert rv.status_code == 200


def test_status_user_with_filter1(client):
    rv = client.get("/users?username=Pe&department=ART-Tanks")
    assert rv.status_code == 200


def test_status_user_with_filter2(client):
    rv = client.get("/users?department=ART-Tanks")
    assert rv.status_code == 200


def test_status_department(client):
    rv = client.get("/department")
    assert rv.status_code == 200


def test_status_department_with_filter(client):
    rv = client.get("/department?name=ART")
    assert rv.status_code == 200


def test_status_user2_negative(client):
    rv = client.get("/ussers")
    assert rv.status_code == 404


def test_text_users(client):
    rv = client.get("/users")
    assert rv.json == {"date_joined": ["25.11.2020.23:15:46", "25.11.2020.23:15:46", "25.11.2020.23:15:46", "25.11.2020"
                                                                                                            ".23:15:46"],
                       "department": ["ART-Tanks", "ART-Maps", "ART-Tanks", "ART-Maps"], "email": ["Pe3oH227@mail.ru",
                                                                                                   "pikriper@gmail.com",
                                                                                                   "pail-max@mail.ru",
                                                                                                   "urets@yandex.ru"],
                       "id": ["a1b", "a2c", "b1b", "b2c"], "username": ["Pe3oH", "Tanya_5", "yeux", "stelhanter"]}


def test_text_users_with_filter_positive(client):
    rv = client.get("/users?username=pe")
    assert rv.json == {'username': ['Pe3oH']}


def test_text_users_with_filter2_positive(client):
    rv = client.get("/users?department=ART-Tanks")
    assert rv.json == {'username': ['Pe3oH', 'yeux']}


def test_text_users_with_filter3_positive(client):
    rv = client.get("/users?username=Pe&department=ART-Tanks")
    assert rv.json == {'username': ['Pe3oH']}


def test_text_users_with_filter3_positive_revert(client):
    rv = client.get("/users?department=ART-Tanks&username=Pe")
    assert rv.json == {'username': ['Pe3oH']}


def test_text_users_with_filter6_low_case_positive(client):
    rv = client.get("/users?username=ye&department=art-tanks")
    assert rv.json == {'username': ['yeux']}


def test_text_users_with_filter6_high_case_positive(client):
    rv = client.get("/users?username=YE&department=ART-TANKS")
    assert rv.json == {'username': ['yeux']}


def test_text_users_with_filter4_negative(client):
    rv = client.get("/users?username=1111")
    assert rv.json == {'username': []}


def test_text_users_with_filter5_negative(client):
    rv = client.get("/users?username=1111&department=ART-Maps")
    assert rv.json == {'username': []}


def test_text_users_with_filter7_negative(client):
    rv = client.get("/users?department=ART-keks")
    assert rv.json == {'username': []}


def test_text_users_with_filter8_negative(client):
    rv = client.get("/users?username=ye&department=art-keks")
    assert rv.json == {'username': []}


def test_text_department_positive1(client):
    rv = client.get("/department")
    assert rv.json == {"departments": ["ART-Tanks", "ART-Maps"]}


def test_text_department__with_filterpositive2(client):
    rv = client.get("/department?name=Tanks")
    assert rv.json == {"departments": ["ART-Tanks"]}


def test_text_department__with_filter_low_case(client):
    rv = client.get("/department?name=tanks")
    assert rv.json == {"departments": ["ART-Tanks"]}


def test_text_department__with_filter_high_case(client):
    rv = client.get("/department?name=tanks")
    assert rv.json == {"departments": ["ART-Tanks"]}


def test_text_department__negative(client):
    rv = client.get("/department?name=kek")
    assert rv.json == {"departments": []}
