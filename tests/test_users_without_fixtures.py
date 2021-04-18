import pytest
import requests
import json
import logging
import os

logging.basicConfig(
    filename="logresults.txt",
    format="%(filename)s:%(lineno)d:%(funcName)s %(message)s")


LOGGER = logging.getLogger(__name__)

def test_status_user():
    rv = requests.get("http://localhost:8080/users")
    if rv.status_code == 200:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.status_code == 200



def test_status_user_with_filter():
    rv = requests.get("http://localhost:8080/users?username=Pe")
    if rv.status_code == 200:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.status_code == 200



def test_status_user_with_filter1():
    rv = requests.get("http://localhost:8080/users?username=Pe&department=ART-Tanks")
    if rv.status_code == 200:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.status_code == 200


def test_status_user_with_filter2():
    rv = requests.get("http://localhost:8080/users?department=ART-Tanks")
    if rv.status_code == 200:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.status_code == 200


def test_status_department():
    rv = requests.get("http://localhost:8080/department")
    if rv.status_code == 200:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.status_code == 200


def test_status_department_with_filter():
    rv = requests.get("http://localhost:8080/department?name=ART")
    if rv.status_code == 200:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.status_code == 200


def test_status_user2_negative():
    rv = requests.get("http://localhost:8080/ussers")
    if rv.status_code == 200:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.status_code == 404


def test_text_users():
    rv = requests.get("http://localhost:8080/users")
    if rv.json() == {'date_joined': ['10.12.2020  0:00:00', '25.01.2020  23:15:46', '11.11.1911  11:11:11', '2.5.2019  15:15:15'],
                     "department": ["ART-Tanks", "ART-Maps", "ART-Tanks", "ART-Maps"], "email": ["Pe3oH227@mail.ru",
                                                                                                 "pikriper@gmail.com",
                                                                                                 "pail-max@mail.ru",
                                                                                                 "urets@yandex.ru"],
                     "id": ["a1b", "a2c", "b1b", "b2c"], "username": ["Pe3oH", "Tanya_5", "yeux", "stelhanter"]}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'date_joined': ['10.12.2020  0:00:00', '25.01.2020  23:15:46', '11.11.1911  11:11:11', '2.5.2019  15:15:15'],
                       "department": ["ART-Tanks", "ART-Maps", "ART-Tanks", "ART-Maps"], "email": ["Pe3oH227@mail.ru",
                                                                                                   "pikriper@gmail.com",
                                                                                                   "pail-max@mail.ru",
                                                                                                   "urets@yandex.ru"],
                       "id": ["a1b", "a2c", "b1b", "b2c"], "username": ["Pe3oH", "Tanya_5", "yeux", "stelhanter"]}


def test_text_users_with_filter_positive():
    rv = requests.get("http://localhost:8080/users?username=pe")
    if rv.json() == {'username': ['Pe3oH']}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': ['Pe3oH']}


def test_text_users_with_filter2_positive():
    rv = requests.get("http://localhost:8080/users?department=ART-Tanks")
    if rv.json() == {'username': ['Pe3oH', 'yeux']}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': ['Pe3oH', 'yeux']}


def test_text_users_with_filter3_positive():
    rv = requests.get("http://localhost:8080/users?username=Pe&department=ART-Tanks")
    if rv.json() == {'username': ['Pe3oH']}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': ['Pe3oH']}


def test_text_users_with_filter3_positive_revert():
    rv = requests.get("http://localhost:8080/users?department=ART-Tanks&username=Pe")
    if rv.json() == {'username': ['Pe3oH']}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': ['Pe3oH']}


def test_text_users_with_filter6_low_case_positive():
    rv = requests.get("http://localhost:8080/users?username=ye&department=art-tanks")
    if rv.json() == {'username': ['yeux']}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': ['yeux']}


def test_text_users_with_filter6_high_case_positive():
    rv = requests.get("http://localhost:8080/users?username=YE&department=ART-TANKS")
    if rv.json() == {'username': ['yeux']}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': ['yeux']}


def test_text_users_with_filter4_negative():
    rv = requests.get("http://localhost:8080/users?username=1111")
    if rv.json() == {'username': []}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': []}


def test_text_users_with_filter5_negative():
    rv = requests.get("http://localhost:8080/users?username=1111&department=ART-Maps")
    if rv.json() == {'username': []}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': []}


def test_text_users_with_filter7_negative():
    rv = requests.get("http://localhost:8080/users?department=ART-keks")
    if rv.json() == {'username': []}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': []}


def test_text_users_with_filter8_negative():
    rv = requests.get("http://localhost:8080/users?username=ye&department=art-keks")
    if rv.json() == {'username': []}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {'username': []}


def test_text_department_positive1():
    rv = requests.get("http://localhost:8080/department")
    if rv.json() == {"departments": ["ART-Tanks", "ART-Maps"]}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {"departments": ["ART-Tanks", "ART-Maps"]}


def test_text_department__with_filterpositive2():
    rv = requests.get("http://localhost:8080/department?name=Tanks")
    if rv.json() == {"departments": ["ART-Tanks"]}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {"departments": ["ART-Tanks"]}


def test_text_department__with_filter_low_case():
    rv = requests.get("http://localhost:8080/department?name=tanks")
    if rv.json() == {"departments": ["ART-Tanks"]}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {"departments": ["ART-Tanks"]}


def test_text_department__with_filter_high_case():
    rv = requests.get("http://localhost:8080/department?name=tanks")
    if rv.json() == {"departments": ["ART-Tanks"]}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {"departments": ["ART-Tanks"]}


def test_text_department__negative():
    rv = requests.get("http://localhost:8080/department?name=kek")
    if rv.json() == {"departments": []}:
        LOGGER.warning('Passed')
    else:
        LOGGER.warning('Failed')
    assert rv.json() == {"departments": []}

if __name__ == '__main__':
    LOGGER.info(' About to start the tests ')
    pytest.main(args=[os.path.abspath(__file__)])
    LOGGER.info(' Done executing the tests ')