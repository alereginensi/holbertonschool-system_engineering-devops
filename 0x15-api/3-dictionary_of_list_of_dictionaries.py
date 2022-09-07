#!/usr/bin/python3
'''
extend your Python script to export data in the JSON format.
'''

if __name__ == "__main__":
    import json
    import requests

    url_all = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    res_all = requests.get(url_all)
    json_all = res_all.json()
    res_user = requests.get(url_user)
    json_user = res_user.json()

    file_name = "todo_all_employees.json"

    final_dic = {}

    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        for user in json_user:
            list_data = []
            for attribute in json_all:
                if attribute["userId"] == user["id"]:
                    dic_data = {}
                    dic_data["username"] = user["username"]
                    dic_data["task"] = attribute["title"]
                    dic_data["completed"] = attribute["completed"]

                    list_data.append(dic_data)

            final_dic[user["id"]] = list_data

        f.write(json.dumps(final_dic))
