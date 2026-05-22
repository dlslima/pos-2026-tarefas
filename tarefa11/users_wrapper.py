import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def list():
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        return response.json()
    else:
        return False


def read(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")

    if response.status_code == 200:
        return response.json()
    else:
        return False


def create(user_data):
    response = requests.post(BASE_URL, json=user_data)

    if response.status_code == 201:
        return response.json()
    else:
        return False


def update(user_id, user_data):
    response = requests.put(f"{BASE_URL}/{user_id}", json=user_data)

    if response.status_code == 200:
        return response.json()
    else:
        return False


def delete(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")

    if response.status_code == 200 or response.status_code == 204:
        return True
    else:
        return False