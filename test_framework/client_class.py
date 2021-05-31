import configparser
import requests


class UserClient:

    def __init__(self, url):
        self.url = url

    def get_users(self, username=None, department=None):
        if username is not None and department is not None:
            response = requests.get(self.url + f"/users/department/{department}/username/{username}")
        elif username is None and department is None:
            response = requests.get(self.url + "/users")
        elif username is not None:
            response = requests.get(self.url + "/users/username/" + f"{str(username)}")
        elif department is not None:
            response = requests.get(self.url + "/users/department/" + f"{str(department)}")
        return response



