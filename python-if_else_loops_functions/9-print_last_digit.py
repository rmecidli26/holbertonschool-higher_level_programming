#!/usr/bin/python3
def print_last_digit(number):
    if(number < 0):
        number = - number
    return number % 10
r = print_last_digit(-1024)
print(r)
