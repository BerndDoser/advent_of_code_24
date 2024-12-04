matrix = []
for line in open('day4/data.txt'):
    code = list(line.strip())
    matrix.append(code)

assert len(matrix) == len(matrix[0])
dim = len(matrix)

# M.S
# .A.
# M.S

codes = ['MSAMS', 'MMASS', 'SMASM', 'SSAMM']

result = 0
for i in range(dim-2):
    for j in range(dim-2):
        code = matrix[i][j] + matrix[i][j+2] + matrix[i+1][j+1] + matrix[i+2][j] + matrix[i+2][j+2]
        if code in codes:
            result += 1

print("answer:", result)
