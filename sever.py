from flask import Flask, request
from stuct import datetime

app = Flask(__name__)

# 使用dict存储用户信息，key为用户名，value为密码
users = {}

# 使用dict存储车辆排队信息，key为用户名，value为车辆信息
vehicles = {}

# 使用dict存储充电桩信息，key为充电桩编号，value为充电桩状态信息
charging_stations = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if username in users:
        return {"message": "Username already exists."}, 400
    users[username] = password
    return {"message": "User created successfully."}, 201

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return {"message": "Login successful."}, 200
    return {"message": "Invalid username or password."}, 400

@app.route('/charging_request', methods=['POST'])
def charging_request():
    username = request.form['username']
    charging_mode = request.form['charging_mode']
    charging_volume = request.form['charging_volume']
    # 需要一些逻辑来生成排队号码，并存储车辆信息
    return {"message": "Charging request submitted successfully."}, 201

@app.route('/charging_detail', methods=['GET'])
def charging_detail():
    username = request.form['username']
    # 需要一些逻辑来生成和返回充电详单信息
    return {"message": "Charging detail returned successfully."}, 200

@app.route('/charging_stations', methods=['GET'])
def get_charging_stations():
    # 需要一些逻辑来返回所有充电桩状态信息
    return {"message": "Charging station information returned successfully."}, 200

if __name__ == '__main__':
    app.run(debug=True)
