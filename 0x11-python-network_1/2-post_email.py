#!/usr/bin/python3
"""
A simple script that takes in a URL and an email address

This module uses urllib to handle HTTP requests
"""

import urllib.request
import urllib.parse
import sys


def send_post_email(url, email):
    """
    Sends a POST request to the specified URL with an email parameter.
    """
    # Data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode()

    # Create a request object
    req = urllib.request.Request(url, data=data)

    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        # Read the response body and decode it from UTF-8
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    # The script takes exactly two arguments
    if len(sys.argv) == 3:
        send_post_email(sys.argv[1], sys.argv[2])
