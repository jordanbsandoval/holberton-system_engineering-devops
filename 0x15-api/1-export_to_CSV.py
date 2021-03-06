#!/usr/bin/python3
"""
gather_data_from_an_API  This module request data from employee API
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) == 2:
        url_base = 'https://jsonplaceholder.typicode.com/users/'
        person_url = '{}{}'.format(url_base, argv[1])
        todos_url = '{}{}/{}'.format(url_base, argv[1], 'todos')

        """ do two request
        one for user personal info and for todos tasks
        """
        person_res = requests.get(person_url)
        todos_res = requests.get(todos_url)

        """ get the obj responses body"""
        person_obj = person_res.json()
        todos_obj = todos_res.json()

        """ working with the data """
        nombre = person_obj['username']
        filename = '{}.csv'.format(person_obj['id'])

        """ open files """
        with open(filename, 'w', newline='') as p:
            for obj in todos_obj:
                linea = [obj['userId'], nombre, obj['completed'], obj['title']]
                writer = csv.writer(p, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL)
                writer.writerow(linea)
