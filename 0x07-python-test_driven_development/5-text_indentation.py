#!/usr/bin/python3
""" Module that prints a text with 2 new
lines after each of these characters:
"""


def text_indentation(text):
    """ Print a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == " ":
        c = c + 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c = c + 1
            while c < len(text) and text[c] == " ":
                c = c + 1
            continue
        c = c + 1
