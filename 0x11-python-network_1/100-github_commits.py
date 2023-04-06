#!/usr/bin/python3
"""
a Python script that takes 2 arguments
The first argument will be the repository name
The second argument will be the owner name
"""
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    try:
        repository = argv[1]
        owner = argv[2]
        url = "https://api.github.com/repos/{}/{}/commits".format(
            owner, repository)
        r = get(url)
        commits = r.json()
        for i in range(0, 10):
            print("{}: {}".format(commits[i].get('sha'),
                                  commits[i]
                                  .get('commit')
                                  .get('author')
                                  .get('name')))
    except Exception as e:
        pass
