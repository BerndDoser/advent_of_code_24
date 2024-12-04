import re

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def get_all_diagonals(matrix):
    diagonals = []

    # Get primary diagonals starting from each element in the first row
    for col in range(len(matrix[0])):
        diagonal = []
        i, j = 0, col
        while i < len(matrix) and j < len(matrix[0]):
            diagonal.append(matrix[i][j])
            i += 1
            j += 1
        diagonals.append(diagonal)

    # Get primary diagonals starting from each element in the first column (excluding the first element)
    for row in range(1, len(matrix)):
        diagonal = []
        i, j = row, 0
        while i < len(matrix) and j < len(matrix[0]):
            diagonal.append(matrix[i][j])
            i += 1
            j += 1
        diagonals.append(diagonal)

    # Get secondary diagonals starting from each element in the first row
    for col in range(len(matrix[0])):
        diagonal = []
        i, j = 0, col
        while i < len(matrix) and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        diagonals.append(diagonal)

    # Get secondary diagonals starting from each element in the last column (excluding the first element)
    for row in range(1, len(matrix)):
        diagonal = []
        i, j = row, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        diagonals.append(diagonal)

    return diagonals

result = 0
matrix = []
for line in open('day4/data.txt'):
    code = list(line.strip())
    matrix.append(code)
    result += len(re.findall('XMAS', line))
    result += len(re.findall('XMAS', line[::-1]))

transposed_matrix = transpose(matrix)
for row in transposed_matrix:
    line = ''.join(row)
    result += len(re.findall('XMAS', line))
    result += len(re.findall('XMAS', line[::-1]))

all_diagonals = get_all_diagonals(matrix)
for diagonal in all_diagonals:
    line = ''.join(diagonal)
    result += len(re.findall('XMAS', line))
    result += len(re.findall('XMAS', line[::-1]))

print("answer:", result)
