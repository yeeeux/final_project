from flask import Flask, request, jsonify
from flask_restful import Api
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


def create_api():
    app = Flask(__name__)

    @app.route('/users', methods=['GET'])
    def users_name(user=None, department=None):
        if 'username' in request.args:
            user = str(request.args['username']).lower()
        if 'department' in request.args:
            department = str(request.args['department']).lower()
        users_list = []
        if user is not None:
            users_from_users_filter = list(filter(lambda x: user.lower() in x.lower(), data_users.keys()))
        if department is not None:
            for departaments in data_users.keys():
                if department.lower() in data_users[departaments]["Department"].lower():
                    users_list.append(departaments)
        if user is not None and department is not None:
            return jsonify(list(set(users_from_users_filter).intersection(users_list)))
        elif user is not None:
            return jsonify(users_from_users_filter)
        elif department is not None:
            return jsonify(users_list)
        else:
            return jsonify(data_users)

    @app.route('/department', methods=['GET'])
    def departs_name(name=None):
        if 'name' in request.args:
            name = str(request.args['name']).lower()
        if name is not None:
            return jsonify(list(filter(lambda x: name.lower() in x.lower(), departments_names)))
        else:
            return jsonify(departments_names)
    return app


if __name__ == '__main__':
    app = create_api()
    app.run(host="0.0.0.0", port=8080, debug=True)  # run our Flask app
