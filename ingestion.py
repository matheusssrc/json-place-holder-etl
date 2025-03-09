import requests

import json
from os import makedirs

RAW_DATA_PATH = "data-lake/raw"
PATH_USERS = "data-lake/raw/users.json"
PATH_TODOS = "data-lake/raw/todos.json"


def collect_raw_data(url: str):
    request = requests.get(url)

    data = request.json()
    
    return data

def save_raw_data(path: str, data: list):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    makedirs(RAW_DATA_PATH, exist_ok=True)

    data_users = collect_raw_data("https://jsonplaceholder.typicode.com/users")

    save_raw_data(PATH_USERS, data_users)

    data_todos = collect_raw_data("https://jsonplaceholder.typicode.com/todos")

    save_raw_data(PATH_TODOS, data_todos)