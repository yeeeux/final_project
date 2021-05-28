from flask import Flask
from flask_restful import Api, Resource
import csv

app = Flask(__name__)
api = Api(app)

data_users = {}
departments_names = []
with open('users_data.csv', "r") as file:
    reader = csv.DictReader(file)
    n = 0
    for line in reader:
        data_users.update({line["username"]: line})
        if line["Department"] not in departments_names:
            departments_names.append(line["Department"])
print(data_users)
print(departments_names)


class Users(Resource):
    def get(self, user=None, department=None):
        users_list = []
        if user is not None:
            for users in data_users.keys():
                if user.lower() in users.lower():
                    users_list.append(users)
            return users_list
        elif department is not None:
            for departaments in data_users.keys():
                if department.lower() in data_users[departaments]["Department"].lower():
                    users_list.append(departaments)
            return users_list
        else:
            return data_users


class Departments(Resource):
    def get(self, name=None):
        department_list = []
        if name is not None:
            for departaments in departments_names:
                if name.lower() in departaments.lower():
                    department_list.append(departaments)
            return department_list
        else:
            return departments_names


api.add_resource(Users, "/users", "/users/username/<string:user>", "/users/departament/<string:department>",
                 endpoint="users")
api.add_resource(Departments, "/department", "/department/name/<string:name>", endpoint="department")

if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app
