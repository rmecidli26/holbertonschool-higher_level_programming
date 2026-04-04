#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(value)
        if(int(value)):
            print(value)
        return True
    except:
        return False
