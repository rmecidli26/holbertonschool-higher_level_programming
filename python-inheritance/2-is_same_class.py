#!/usr/bin/python3
"""Module for is_same_class"""


def is_same_class(obj, a_class):
    """Function that returns True if object is exactly an instance"""
    return type(obj) is a_class
