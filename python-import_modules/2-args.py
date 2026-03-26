#!/usr/bin/python3
import sys
n = len(sys.argv) - 1
if __name__ == "__main__":
    if n == 0:
        print("{} arguments.".format(n))    
    if n >= 1:
        print("{} argument: ".format(n))
        for i in range(1, n+1):
            print("{}: {}".format(i, sys.argv[i]))
