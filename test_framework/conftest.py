import pytest
import logging
from _pytest.runner import CallInfo
from client_class import UserClient
from client_class import DepartClient
import configparser

parser = configparser.ConfigParser()
parser.read("C:\\git\\final_project\\test_framework\\config.ini")
URL = parser.get("test_framework", "SERVICE_URL")


@pytest.fixture(scope="function")
def client():
    app = UserClient(URL)
    return app.get_users


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)


@pytest.fixture(scope="function")
def depart_client():
    app = DepartClient(URL)
    return app.get_departs


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)