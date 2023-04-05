#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POSTrequest
to http://0.0.0.0:5000/search_user with the letter as aparameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    value = {'q': "" if len(argv) < 2 else argv[1]}

    try:
        request = requests.post(url, value)
        dic = request.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as error:
        print("Not a valid JSON")
