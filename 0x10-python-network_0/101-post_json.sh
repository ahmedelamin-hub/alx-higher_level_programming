#!/bin/bash
# Sends a JSON POST request to a URL with the response body
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
