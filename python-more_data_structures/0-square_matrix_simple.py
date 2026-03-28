#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = matrix[:]
    new_a = []
    for i in range(0, len(matrix)):
        new = []
        for j in range(0, len(matrix[i])):
            temp = matrix[i][j] * matrix[i][j]
            new.append(temp)
        new_a.append(new)
    return new_a
