#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for i in sorted_keys:
        print("{}: {}".format(i, a_dictionary[i]))


def simple_delete(a_dictionary, key=""):
    for i in range(0, a_dictionary.keys()):
        if key in a_dictionary.keys():
            del a_dictionary[key]
