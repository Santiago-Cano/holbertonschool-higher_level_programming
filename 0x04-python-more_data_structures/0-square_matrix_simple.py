#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    newmatrix = []
    for i in range(len(matrix)):
        newmatrix.append(list(map(lambda i: i*i, matrix[i])))
    return (newmatrix)
