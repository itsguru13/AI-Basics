matrix1 = [
    [1, 1, 3],
    [2, 2, 4],
    [3, 3, 5]
]

transpose = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        transpose[i][j] = matrix1[j][i]

for r in transpose:
    print(r)