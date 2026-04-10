#!/usr/bin/python3
"""Module for inherits_from"""


def inherits_from(obj, a_class):
    """Check if obj is an inherited instance of a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
