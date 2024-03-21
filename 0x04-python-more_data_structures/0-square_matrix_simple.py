#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	rows = len(matrix)
	cols = len(matrix[0])

	result = [[0 for _ in range(rows)] for _ in range(cols)]

	for i in range(rows):
		for j in range(cols):
			result[i][j] = matrix[i][j] ** 2

	return result
