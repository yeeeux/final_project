import json
from flask import Flask, request, jsonify
import logging

logging.basicConfig(filename="api.log",
                    level=logging.INFO,
                    format=f"%(asctime)s - [%(levelname)s] - %(name)s - "
                           f"(%("f"filename)s).%(funcName)s(%(lineno)d) - "
                           f"%("f"message)s")

logger = logging.getLogger(__name__)

with open("users_data.json", "r") as file:
    logger.info("File with data was opened")
    data_users = json.load(file)


def get_user_from_username(
        data_filter: str = None,
        username: str = None) \
        -> list:
    """ Function for search users by username in data.
    :param data_filter: Where in data we will search username.
    :param username: Username that we want to find in data.
    :return: list of users with "username" inside of them.
    """
    logger.info(f"function 'get_user_from_username' get: {data_filter}, {username}")
    # Getting all list of users
    value_list = [item[data_filter] for item in data_users["users"] if data_filter in item.keys()]
    # Find in all users value
    answer = list(set(filter(lambda user: username.lower() in user.lower(), value_list)))
    logger.info(f"function 'get_user_from_username' return: {answer}")
    return answer


def get_user_from_other_param(
        return_param: str,
        choice_param: str,
        value_choice_param: str) \
        -> list:
    """ Function for search users by other parameter in data
        :param return_param: What parameters we want getting
        :param choice_param: What parameters we use for searching users
        :param value_choice_param: searching value

        :return: List of users with needed department
        """
    logger.info(f"get_user_from_other_param' get {return_param, choice_param, value_choice_param}")
    # Getting list of users and list of departments
    list_of_users = [item[return_param] for item in data_users["users"] if return_param in item.keys()]
    list_of_departments = [item[choice_param] for item in data_users["users"] if choice_param in item.keys()]
    # getting dictionary with pair user:department
    dictionary_values = dict(zip(list_of_users, list_of_departments))
    # Find needed users
    answer = [item for item in dictionary_values.keys() if value_choice_param.lower() in dictionary_values[item].lower()]
    logger.info(f"function 'get_user_from_other_param' return {answer}")
    return answer


def create_api():
    app_api = Flask(__name__)

    @app_api.route('/users', methods=['GET'])
    def users_name():
        user = request.args.get("username")
        department = request.args.get("department")
        logger.info(f"function 'users_name' get username = {user}, department = {department}")
        # Searching in database
        if user:
            return jsonify(get_user_from_username("username", user))
        if department:
            return jsonify(get_user_from_other_param("username", "department", department))
        else:
            return jsonify(data_users)

    @app_api.route('/departments', methods=['GET'])
    def departs_name():
        departament_name = request.args.get("name")
        logger.info(f"function 'departs_name' get name = {departament_name}")
        if departament_name:
            return jsonify(get_user_from_username("department", departament_name))
        else:
            return jsonify(list(set(item["department"] for item in data_users["users"] if "department" in item.keys())))

    return app_api


if __name__ == '__main__':
    app = create_api()
    app.run(host="0.0.0.0", port=8000, debug=False)  # run our Flask app
