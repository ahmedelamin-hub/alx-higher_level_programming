#!/bin/bash
# Sends a GET request custom header and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
