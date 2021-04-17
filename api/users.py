import pandas as pd
from flask import Flask, request, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

data = pd.read_csv('users_data.csv')  # read CSV
data = data.to_dict()  # convert dataframe to dictionary


def create_app():
    app = Flask(__name__)

    @app.route('/users', methods=['GET'])
    def users_name():
        results1 = []
        results1_id = []
        results1_email = []
        results1_department = []
        results1_join = []
        results2 = []
        results3 = []
        tumbler1 = False
        tumbler2 = False
        if 'username' in request.args:
            user = str(request.args['username']).lower()
            tumbler1 = True

            for users in data.keys():
                if users == "username":
                    for i in (data[users].values()):
                        if user in i.lower():
                            results1.append(i)
        else:
            for unit in data.keys():
                if unit == "username":
                    for i in (data[unit].values()):
                        results1.append(i)
                elif unit == "userId":
                    for i in (data[unit].values()):
                        results1_id.append(i)
                elif unit == "email":
                    for i in (data[unit].values()):
                        results1_email.append(i)
                elif unit == "Department":
                    for i in (data[unit].values()):
                        results1_department.append(i)
                elif unit == "data_joined":
                    for i in (data[unit].values()):
                        results1_join.append(i)

        if 'department' in request.args:
            depart = str(request.args['department']).lower()
            tumbler2 = True
            for depa in data.keys():
                if depa == "Department":
                    for i in (data[depa].keys()):
                        if depart == data[depa][i].lower():
                            results2.append(data['username'][i])
        print(results1)
        print(results2)

        for item in results1:
            if item in results2:
                results3.append(item)

        if not tumbler1 and not tumbler2:
            return jsonify(username=results1,
                           id=results1_id,
                           email=results1_email,
                           department=results1_department,
                           date_joined=results1_join)
        elif tumbler1 and not tumbler2:
            return jsonify(username=results1)
        else:
            return jsonify(username=results3)

    @app.route('/department', methods=['GET'])
    def departs_name():
        dep_result1 = []
        if 'name' in request.args:
            departament = str(request.args['name']).lower()

            for departmen in data.keys():
                if departmen == "Department":
                    for i in (data[departmen].values()):
                        if departament in i.lower():
                            if i not in dep_result1:
                                dep_result1.append(i)
        else:
            for unit in data.keys():
                if unit == "Department":
                    for i in (data[unit].values()):
                        if i not in dep_result1:
                            dep_result1.append(i)
        return jsonify(departments=dep_result1)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080)  # run our Flask app
