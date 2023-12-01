#!/bin/bash
# Script sends a JSON POST request to a URL first argument
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
