
def test_status_user(client):
    rv = client()
    assert rv.status_code == 200


def test_status_user_with_filter(client):
    rv = client("pe")
    assert rv.status_code == 200


def test_status_user_with_filter1(client):
    rv = client("pe", "ART-Tanks")
    assert rv.status_code == 200


def test_status_user_with_filter2(client):
    rv = client(None, "ART-Tanks")
    assert rv.status_code == 200


def test_status_department(depart_client):
    rv = depart_client()
    assert 200 == rv.status_code


def test_status_department_with_filter(depart_client):
    rv = depart_client("ART")
    assert 200 == rv.status_code


def test_text_users(client):
    rv = client()
    assert rv.json() == {
        "items": [
            {
                "Department": "ART-Tanks",
                "data_joined": "10.12.2020  0:00:00",
                "email": "Pe3oH227@mail.ru",
                "userId": "a1b",
                "username": "Pe3oH"
            },
            {
                "Department": "ART-Maps",
                "data_joined": "25.01.2020  23:15:46",
                "email": "pikriper@gmail.com",
                "userId": "a2c",
                "username": "Tanya_5"
            },
            {
                "Department": "ART-Maps",
                "data_joined": "2.5.2019  15:15:15",
                "email": "urets@yandex.ru",
                "userId": "b2c",
                "username": "stelhanter"
            },
            {
                "Department": "ART-Tanks",
                "data_joined": "11.11.1911  11:11:11",
                "email": "pail-max@mail.ru",
                "userId": "b1b",
                "username": "yeux"
            }
        ]
    }


def test_text_users_with_filter_positive(client):
    rv = client("Pe")
    assert rv.json() == ['Pe3oH']


def test_text_users_with_filter2_positive(client):
    rv = client(None, "ART-Tanks")
    assert rv.json() == ['Pe3oH', 'yeux']


def test_text_users_with_filter3_positive(client):
    rv = client("Pe", "ART-Tanks")
    assert rv.json() == ['Pe3oH']


def test_text_users_with_filter6_low_case_positive(client):
    rv = client("ye", "art-tanks")
    assert rv.json() == ['yeux']


def test_text_users_with_filter6_high_case_positive(client):
    rv = client("YE", "ART-TANKS")
    assert rv.json() == ['yeux']


def test_text_users_with_filter4_negative(client):
    rv = client("1111")
    assert rv.json() == []


def test_text_users_with_filter5_negative(client):
    rv = client("1111", "ART-Maps")
    assert [] == rv.json()


def test_text_users_with_filter7_negative(client):
    rv = client(None, "ART-keks")
    assert rv.json() == []


def test_text_users_with_filter8_negative(client):
    rv = client("ye", "art-keks")
    assert rv.json() == []


def test_text_department_positive1(depart_client):
    rv = depart_client()
    assert rv.json() == ["ART-Tanks", "ART-Maps1"]


def test_text_department_with_filterpositive2(depart_client):
    rv = depart_client("Tanks")
    assert rv.json() == ["ART-Tanks"]


def test_text_department_with_filter_low_case(depart_client):
    rv = depart_client("tanks")
    assert rv.json() == ["ART-Tanks"]


def test_text_department_with_filter_high_case(depart_client):
    rv = depart_client("TANKS")
    assert rv.json() == ["ART-Tanks"]


def test_text_department_negative(depart_client):
    rv = depart_client("jek")
    assert rv.json() == []
