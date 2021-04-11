import pandas as pd
from flask import Flask, request, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

data = pd.read_csv('users.csv')  # read CSV
data = data.to_dict()  # convert dataframe to dictionary


@app.route('/users', methods=['GET'])
def users_name():
    results1 = []
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

    if 'department' in request.args:

        depart = str(request.args['department']).lower()
        tumbler2 = True
        for depa in data.keys():
            if depa == "Department":
                for i in (data[depa].keys()):
                    if depart == data[depa][i]:
                        results2.append(data['username'][i])

    if results1 != [] and results2 != []:
        for item in results1:
            if item in results2:
                results3.append(item)
        if tumbler1 == False:
            return (f'Пользователи в отделе {depart} %s' % results3)
        else:
            return (f'Пользователи в отделе {depart} с вхождением {user}: %s' % results3)
    elif results1 != [] and results2 == []:
        return jsonify('data: %s' % results1)
    elif results2 != [] and results1 == []:
        return jsonify('data: %s' % results2)
    else:
        if tumbler2 == False:
            return f"Отсутствуют пользоватили с вхождением {user}:"
        else:
            return f"Отсутствуют пользоватили в отделе {depart} с вхождением {user}:"




# api.add_resource(Users, '/users')
# api.add_resource(Departments, '/departments')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # run our Flask app
