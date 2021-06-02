import json
from flask import Flask, request, jsonify
import logging

logging.basicConfig(filename="api.log",
                    level=logging.ERROR,
                    format=f"%(asctime)s - [%(levelname)s] - %(name)s - "
                           f"(%("f"filename)s).%(funcName)s(%(lineno)d) - "
                           f"%("f"message)s")

logger = logging.getLogger(__name__)

with open("users_data.json", "r") as file:
    logger.info("File with data was opened")
    data_users = json.load(file)


def find_user(key: str, value: str):
    """
    Function for search users
    :param key:
    :param value:
    :return: needed users
    """
    logger.info(f"function 'return_value' get {key}")
    # Getting all list of users
    value_list = [item[key] for item in data_users["users"] if key in item.keys()]
    # Find in all users value
    answer = list(set(filter(lambda x: value.lower() in x.lower(), value_list)))
    return answer


def find_user_not_from_username(find: str, refund: str, value: str):
    """
    Function for search users from any filter
    :param find: What parameters we want getting
    :param refund: What parameters we use for searching users
    :param value: searching value
    :return: needed users from some filter
    """
    logger.info(f"function 'return_another_value' get {find, refund}")
    # Getting list of users and list of departments
    answer_1 = [item[find] for item in data_users["users"] if find in item.keys()]
    answer_2 = [item[refund] for item in data_users["users"] if refund in item.keys()]
    # getting dictionary with pair user:department
    dictionary_values = dict(zip(answer_1, answer_2))
    # Find needed users
    answer = [item for item in dictionary_values.keys() if value.lower() in dictionary_values[item].lower()]
    logger.info(f"function 'return_another_value' return {dictionary_values}")
    return answer


def create_api():
    app_api = Flask(__name__)

    @app_api.route('/users', methods=['GET'])
    def users_name():
        user = request.args.get("username")
        department = request.args.get("department")

        logger.info(f"function 'users_name' get username = {user}, department = {department}")
        # Searching in database
        if user is not None:
            return jsonify(find_user("username", user))
        if department is not None:
            return jsonify(find_user_not_from_username("username", "department", department))
        else:
            return jsonify(data_users)

    @app_api.route('/department', methods=['GET'])
    def departs_name():
        name = request.args.get("name")
        logger.info(f"function 'departs_name' get name = {name}")
        if name is not None:
            return jsonify(find_user("department", name))
        else:
            return jsonify(list(set(item["department"] for item in data_users["users"] if "department" in item.keys())))

    return app_api


if __name__ == '__main__':
    app = create_api()
    app.run(host="0.0.0.0", port=8000, debug=True)  # run our Flask app
