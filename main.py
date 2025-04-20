import csv

import requests

try:
    response = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    with open('my_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'completed', 'userId']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(response)
except:
    print("Failed To Fetch!")