#!/usr/bin/python3
"""
Python script that takes in a URL and displays the value of the X-Request-Id
"""
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
