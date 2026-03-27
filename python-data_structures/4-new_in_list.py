#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list = my_list[:]
    if idx < 0 or len(my_list) < idx:
        return my_list
    elif idx >= 0:
        my_list[idx] = element
        return my_list