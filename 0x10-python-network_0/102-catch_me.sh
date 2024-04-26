#!/bin/bash
# This script makes a request to a specific endpoint
curl -sL -X PUT "0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool" -d "user_id=98" -w "%{http_code}" -o /dev/null
