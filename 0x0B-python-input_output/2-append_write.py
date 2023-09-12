#!/usr/bin/python3
"""Append to a file module"""


def append_write(filename="", text=""):
    """ Append to a file function"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
