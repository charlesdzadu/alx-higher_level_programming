#!/bin/bash
# Displays only the status code of the response
curl -sLw "%{http_code}" -o /dev/null "$1"
