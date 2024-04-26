#!/usr/bin/python3
"""
A simple script that takes in a URL, sends a request

This module demonstrates the use of urllib to manage HTTP requests
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Sends an HTTP request to the given URL and prints the value of the
    'X-Request-Id' header from the response.
    """
    with urllib.request.urlopen(url) as response:
        # Retrieve the X-Request-Id
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    # The URL is taken from the command-line arguments
    if len(sys.argv) > 1:
        fetch_x_request_id(sys.argv[1])
