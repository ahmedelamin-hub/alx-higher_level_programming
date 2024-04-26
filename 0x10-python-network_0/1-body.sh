#!/bin/bash
# This script sends a GET request to a Url
curl -s -L "$1" -o /dev/stdout -w '%{http_code}' | grep -q '^200$' && cat /dev/stdout
