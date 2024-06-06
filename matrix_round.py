'''
A matrix (two-dimensional array) consisting of integers is given as input.
You need to rotate the matrix 90 degrees clockwise.
'''

'''
На вход подается матрица (двумерный массив), состоящая из целых чисел.
Необходимо повернуть матрицу на 90 градусов по часовой стрелке.
'''


def matrix_round(matrix):
    round_matrix = []
    for i in range(len(matrix[0])):
        round_matrix.append(list())
    for col in range(len(matrix[0])):
        for raw in range(len(matrix)):
            round_matrix[col].insert(0, matrix[raw][col])
    return round_matrix


def show_matrix(matrix):
    for raw in matrix:
        raw = list(map(str, raw))
        print(" ".join(raw))
    print("\n")


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix_2 = [[1, 2],
            [4, 5],
            [7, 8]]

show_matrix(matrix)
first = matrix_round(matrix)
show_matrix(first)
second = matrix_round(first)
show_matrix(second)
third = matrix_round(second)
show_matrix(third)
fourth = matrix_round(third)
show_matrix(fourth)
