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


def get_user_by_username(
        username: str = None) \
        -> list:
    """ Function for search users by username in data.
    :param username: Username that we want to find in data.
    :return: list of users with "username" inside of them.
    """
    logger.info(f"get: {username}")
    suitable_users = [user for user in data_users["users"] if username.lower() in user["username"].lower()]
    logger.info(f"return: {suitable_users}")
    return suitable_users


def get_user_by_department(
        department: str) \
        -> list:
    """ Function for search users by department in data
        :param department: User in department that we want to find in data.
        :return: List of users with needed department
        """
    logger.info(f"get {department}")
    suitable_users = [user for user in data_users["users"] if department.lower() in user["department"].lower()]
    logger.info(f"return {suitable_users}")
    return suitable_users


def get_user_by_username_or_department(
        username: str = None,
        department: str = None) \
        -> list:
    """ Function for search users by department and username in data
    :param department: User in department that we want to find in data.
    :param username: Username that we want to find in data.
    :return: list of users with "username" inside of them.
    """
    logger.info(f"get: {username, department}")
    suitable_users = [user for user in data_users["users"] if username.lower() in user["username"].lower() and
                      department.lower() in user["department"].lower()]
    logger.info(f"return: {suitable_users}")
    return suitable_users


def create_api():
    app_api = Flask(__name__)

    @app_api.route('/users', methods=['GET'])
    def users():
        user = request.args.get("username")
        department = request.args.get("department")
        logger.info(f"function get username = {user}, department = {department}")
        # Searching in database
        if user and department:
            return jsonify(get_user_by_username_or_department(user, department))
        if user:
            return jsonify(get_user_by_username(user))
        if department:
            return jsonify(get_user_by_department(department))
        else:
            return jsonify(data_users)

    @app_api.route('/departments', methods=['GET'])
    def departments():
        departament_name = request.args.get("name")
        logger.info(f"function get name = {departament_name}")
        if departament_name:
            return jsonify(get_user_by_username_or_department("department", departament_name))
        else:
            return jsonify(list(set(item["department"] for item in data_users["users"] if "department" in item.keys())))

    return app_api


if __name__ == '__main__':
    app = create_api()
    app.run(host="0.0.0.0", port=8000, debug=False)  # run our Flask app
