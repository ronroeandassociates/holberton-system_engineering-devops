#!/usr/bin/python3

'''
    Python script that, using this REST API
    for a given employee ID
    returns information about his/her
    TODO list progress
    export data in the JSON format
'''


import json
import requests
import sys


if __name__ == '__main__':
    id_c = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id_c}"
    ).json()

    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"
    ).json()


    with open(f"{id_c}.json", "w") as user_id:
        json.dump({id_c: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': users.get('username')
        } for task in todos]}, user_id)
