# n = int(input("Enter a number from 2 to 10"))
n = 8
matrix = list()
matrix2 = list()
m = n * n
for x in range(n):
    for y in range(n):
        matrix2.append(0)
    matrix.append(matrix2)


def display_matrix(list_):
    for i in range(n):
        for j in range(n):
            print(list_[i][j], end=" ")
        print(" ")


x = 0
y = 0
k = 1
v = 1
a = 1
while a:
    while (matrix[x][y] == 0) & (y < n):
        matrix[x][y] = v
        print(x, y, matrix[x][y], end=" H ")
        y += 1
        v += 1
    k = v
    if k == 64:
        a = 0
    while (matrix[x][y] == 0) & (x < n):
        x += 1
        matrix[x][y] = v
        print(x, y, matrix[x][y], end=" H ")
        v += 1
    k = v
    if k == 64:
        a = 0
    while (matrix[x][y] == 0) & (x >= 0):
        matrix[x][y] = k
        x -= 1
        v += 1
    k = v
    if k == 64:
        a = 0
    while (matrix[x][y] == 0) & (y >= 0):
        matrix[x][y] = k
        y -= 1
        k = v
    k = v
    if k == 64:
        a = 0
