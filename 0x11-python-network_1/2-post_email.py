#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
