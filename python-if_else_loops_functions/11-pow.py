#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(b):
            result = result * a
    elif b == 0:
        result
    else:
        for i in range(-b):
            result = result * (1/a)
    return result
