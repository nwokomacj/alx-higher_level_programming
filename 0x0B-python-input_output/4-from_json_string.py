#!/usr/bin/python3
"""Defines a JSON to python-object function"""
import json


def from_json_string(my_str):
    """Return the python object representation of a JSON string"""
    return json.loads(my_str)
