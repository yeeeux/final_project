import pytest
import logging
from _pytest.runner import CallInfo
from Client import UserClient
import os
import configparser
import json
from random import randint

parser = configparser.ConfigParser()
parser.read("config.ini")
default_URL = parser.get("test_framework", "SERVICE_URL")
URL = os.environ.get("SERVICE_URL", default_URL)


@pytest.fixture
def client():
    app = UserClient(URL)
    return app.get_users


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)


@pytest.fixture
def random_user_data():
    with open("users_data.json", "r") as file:
        data_users = json.load(file)
    max_value = len(data_users["users"])-1
    random_value = randint(0, max_value)
    return data_users["users"][random_value]
