import requests

# 设置服务器的基础URL
BASE_URL = 'http://127.0.0.1:5000'

def register(username, password):
    # 使用POST请求发送用户注册信息到服务器
    response = requests.post(f'{BASE_URL}/register', data={'username': username, 'password': password})

    # 返回服务器的响应
    if response.status_code == 200:
        print('Registration successful.')
        return True
    else:
        print('Registration failed.')
        return False
def login(username, password):
    # 使用POST请求发送用户登录信息到服务器
    response = requests.post(f'{BASE_URL}/login', data={'username': username, 'password': password})

    # 返回服务器的响应
    if response.status_code == 200:
        print('Login successful.')
        return True
    else:
        print('Login failed.')
        return False

def charging_request(username, charging_mode, charging_volume):
    response = requests.post(f'{BASE_URL}/charging_request', data={'username': username, 'charging_mode': charging_mode, 'charging_volume': charging_volume})
    print(response.json())

def charging_detail(username):
    response = requests.get(f'{BASE_URL}/charging_detail', data={'username': username})
    print(response.json())

def main():
    username = 'test'
    password = 'test123'
    register(username, password)
    login(username, password)
    charging_request(username, 'fast', 50)
    charging_detail(username)

if __name__ == '__main__':
    main()
