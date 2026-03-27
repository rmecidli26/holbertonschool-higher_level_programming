#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_my_list = my_list[:]
    if idx < 0 or len(my_list) - 1 < idx:
        return new_my_list
    elif idx >= 0:
        new_my_list[idx] = element
        return new_my_list
