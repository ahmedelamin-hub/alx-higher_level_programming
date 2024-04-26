#!/usr/bin/python3
"""
Takes in a URr/sends a request to the URL, then displaysvalue
of the X-Request-Id
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
