#!/usr/bin/python3
"""
Script that takes in a URL and an email address, and sends a POST request
"""
import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
