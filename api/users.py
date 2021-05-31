from flask import Flask
from flask_restful import Api, Resource
import csv


app = Flask(__name__)
api = Api(app)

data_users = {}
departments_names = []
with open('users_data.csv', "r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        data_users.update({line["username"]: line})
        if line["Department"] not in departments_names:
            departments_names.append(line["Department"])

class Users(Resource):
    def get(self, user=None, department=None):
        users_list = []
        if user is not None:
            users_from_users_filter = list(filter(lambda x: user.lower() in x.lower(), data_users.keys()))
        if department is not None:
            for departaments in data_users.keys():
                if department.lower() in data_users[departaments]["Department"].lower():
                    users_list.append(departaments)
        if user is not None and department is not None:
            return list(set(users_from_users_filter).intersection(users_list))
        elif user is not None:
            return users_from_users_filter
        elif department is not None:
            return users_list
        else:
            return data_users


class Departments(Resource):
    def get(self, name=None):
        if name is not None:
            return list(filter(lambda x: name.lower() in x.lower(), departments_names))
        else:
            return departments_names


api.add_resource(Users, "/users", "/users/username/<string:user>", "/users/department/<string:department>",
                 "/users/department/<string:department>/username/<string:user>",
                 "/users/username/<string:user>/department/<string:department>", endpoint="users")
api.add_resource(Departments, "/department", "/department/name/<string:name>", endpoint="department")

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=8080, debug=True)  # run our Flask app
