#!/usr/bin/python3
"""
URL and an email, sends a POST request to the URL with the
email as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)