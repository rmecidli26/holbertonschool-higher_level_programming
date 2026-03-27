#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                print()
            if j == len(matrix[0]) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]),end=" ")
