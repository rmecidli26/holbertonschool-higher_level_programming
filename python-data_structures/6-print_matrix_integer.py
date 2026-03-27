#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
    if not row:  # Bu, 'if len(row) == 0:' deməkdir
        print()
        break
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if j == len(matrix[0]) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]),end=" ")
