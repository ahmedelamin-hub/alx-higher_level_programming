#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the urllib package.

"""
import urllib.request


def fetch_status(url):
    """
    status from the given URL and prints detail
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_status("https://alx-intranet.hbtn.io/status")
