import json
from flask import Flask, request, jsonify
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


departments_names = []
with open("users_data.json", "r") as file:
    data_users = json.load(file)


def return_value(value: str):
    """
    Function for getting needed values from key: value
    :param value:
    :return: list with values
    """
    answer_list = []
    for item in data_users["items"]:
        if value in item.keys():
            if item[value] not in answer_list:
                answer_list.append(item[value])
    return answer_list


def return_another_value(find: str, refund: str):
    """
    Function for getting a dictionary with a pair refund:find
    :param find:
    :param refund:
    :return: dictionary with values from database with pair refund:find
    """
    answer_1 = []
    answer_2 = []
    for item in data_users["items"]:
        if find in item.keys():
            answer_1.append(item[find])
        if refund in item.keys():
            answer_2.append(item[refund])
    return dict(zip(answer_2, answer_1))


def create_api():
    app_api = Flask(__name__)

    @app_api.route('/users', methods=['GET'])
    def users_name(user=None, department=None):
        users_list = []
        users_from_users_filter = []
        # Getting the values username and department from get request
        if 'username' in request.args:
            user = str(request.args['username']).lower()
        if 'department' in request.args:
            department = str(request.args['department']).lower()
        # Searching in database
        if user is not None:
            users_from_users_filter = list(filter(lambda x: user.lower() in x.lower(), return_value("username")))
        if department is not None:
            buffer_dictionary = return_another_value("Department", "username")
            for item in buffer_dictionary.keys():
                if department.lower() in buffer_dictionary[item].lower():
                    users_list.append(item)
        if user is not None and department is not None:
            return jsonify(list(set(users_from_users_filter).intersection(users_list)))
        elif user is not None:
            return jsonify(users_from_users_filter)
        elif department is not None:
            return jsonify(users_list)
        else:
            return jsonify(data_users)

    @app_api.route('/department', methods=['GET'])
    def departs_name(name=None):
        if 'name' in request.args:
            name = str(request.args['name']).lower()
        if name is not None:
            return jsonify(list(filter(lambda x: name.lower() in x.lower(), return_value("Department"))))
        else:
            return jsonify(return_value("Department"))

    return app_api


if __name__ == '__main__':
    app = create_api()
    app.run(host="0.0.0.0", port=8080, debug=True)  # run our Flask app
