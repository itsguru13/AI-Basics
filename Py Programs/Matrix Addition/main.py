matrix1 = [
    [1, 1, 3],
    [2, 2, 4],
    [3, 3, 5]
]

matrix2 = [
    [3, 3, 4],
    [4, 4, 5],
    [5, 5, 6]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

for r in result:
    print(r)