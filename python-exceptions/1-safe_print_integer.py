#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if(int(value) == True):
            print(value)
        return True
    except:
        return False
