#!/usr/bin/python3
"""Defines a text file - reading () function"""


def read_file(filename=""):
    """prints the content of a UTF-8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
