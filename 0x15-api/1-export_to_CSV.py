#!/usr/bin/python3
'''
extend your Python script to export data in the CSV format.
'''

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    try:
        ID = argv[1]

        url_all = "https://jsonplaceholder.typicode.com/todos?userId={}"\
            .format(ID)
        url_user = "https://jsonplaceholder.typicode.com/users/{}".format(ID)

        res_all = requests.get(url_all)
        json_all = res_all.json()
        res_user = requests.get(url_user)
        json_user = res_user.json()
        file_name = ID + ".csv"

        with open(file_name, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for attribute in json_all:
                userId = attribute["userId"]
                user_name = json_user["username"]
                task_status = attribute["completed"]
                title = attribute["title"]
                data = [userId, user_name, task_status, title]
                writer.writerow(data)

    except Exception as error:
        print("Error message: {}".format(error))
