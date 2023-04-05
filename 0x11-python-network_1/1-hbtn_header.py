#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header of the response. """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        print(response.headers['X-Request-Id'])
