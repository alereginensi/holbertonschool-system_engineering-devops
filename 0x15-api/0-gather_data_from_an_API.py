#!/usr/bin/python3
'''
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''

if __name__ == "__main__":
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

        EMPLOYEE_NAME = json_user["name"]
        NUMBER_OF_DONE_TASKS = 0
        TOTAL_NUMBER_OF_TASKS = 0
        TASK_TITLE = []
        for task in json_all:
            TOTAL_NUMBER_OF_TASKS += 1
            if task["completed"] is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(task["title"])

        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))

        for task in TASK_TITLE:
            print("\t {}".format(task))

    except Exception as error:
        print("Error message: {}".format(error))
