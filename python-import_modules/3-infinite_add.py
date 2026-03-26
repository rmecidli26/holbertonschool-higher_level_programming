#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv) - 1
    sum = 0
    for i in range(1, n+1):
        sum = sum + int(sys.argv[i])
    print("{}".format(sum))
