#!/bin/bash
# This script sends an OPTIONS request to the allowed HTTP methods
curl -s -X OPTIONS "$1" -I | grep "Allow:" | cut -d " " -f2-
