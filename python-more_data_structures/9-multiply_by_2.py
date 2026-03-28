#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for i in sorted_keys:
        print("{}: {}".format(i, a_dictionary[i]))


def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}
