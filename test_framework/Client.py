import requests


class UserClient:

    def __init__(self, url):
        self.url = url

    def __get(self,  username: str, department: str, endpoint: str):
        if not endpoint:
            response = requests.get(self.url + "/users", params={"username": username, "departament": department})
        elif endpoint == "departments":
            response = requests.get(self.url + "/departments", params={"name": department})
        return response

    def get_users(self, username: str = None, department: str = None, endpoint=None):
        users = self.__get(username, department, endpoint)
        return users
