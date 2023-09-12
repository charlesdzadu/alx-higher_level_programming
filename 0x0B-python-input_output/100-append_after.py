#!/usr/bin/python3
"""Append after module"""


def append_after(filename="", search_string="", new_string=""):
    """Append after function"""
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
        f.seek(0)
        f.writelines(lines)
