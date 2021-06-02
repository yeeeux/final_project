import pytest
import logging
from _pytest.runner import CallInfo
from client_class import UserClient, DepartClient
import os
import configparser

parser = configparser.ConfigParser()
parser.read("config.ini")
default_URL = parser.get("test_framework", "SERVICE_URL")
URL = os.environ.get("SERVICE_URL", default_URL)


@pytest.fixture()
def client():
    app = UserClient(URL)
    return app.get_users


@pytest.fixture()
def depart_client():
    app = DepartClient(URL)
    return app.get_departs


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)