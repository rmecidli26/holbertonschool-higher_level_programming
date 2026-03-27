#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) <= idx:
        return my_list
    elif idx <= len(my_list) - 1:
        my_list[idx] = element
        return my_list
