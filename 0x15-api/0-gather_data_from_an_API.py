#!/usr/bin/python3
"""gather_data_from_an_API  This module request data from employee API"""

import requests
import sys



# Process functions
def make_request(id):
    """make request"""
    user_r = "https://jsonplaceholder.typicode.com/users/" + id
    todo_r = "https://jsonplaceholder.typicode.com/todos/?userId=" + id
    dato = [requests.get(user_r).json(), requests.get(todo_r).json()]
    return(data)


def print_data(data):
    """print data json"""
    user_name = data[0]["name"]
    tarea_completa = 0
    task = 0

    for i in data[1]:
        task += 1
        if i['completed']:
            tarea_completa += 1

    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          completed_task,
                                                          task))

    for item in data[1]:
        if item['completed'] is True:
            print('\t {}'.format(item['title']))


def main():
    if len(sys.argv) == 2:
        dato = make_request(sys.argv[1])
        print_data(dato)


if __name__ == "__main__":
    main()
