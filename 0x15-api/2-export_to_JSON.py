#!/usr/bin/python3
'''
extend your Python script to export data in the JSON format.
'''

if __name__ == "__main__":
    import json
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
        file_name = ID + ".json"

        final_dic = {}
        list_data = []
        with open(file_name, 'w', encoding='UTF8', newline='') as f:
            for attribute in json_all:
                dic_data = {}
                dic_data["task"] = attribute["title"]
                dic_data["completed"] = attribute["completed"]
                dic_data["username"] = json_user["username"]
                list_data.append(dic_data)

            final_dic[ID] = list_data
            f.write(json.dumps(final_dic))

    except Exception as error:
        print("Error message: {}".format(error))
