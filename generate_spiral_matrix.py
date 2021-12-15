"""GENERATE A SPIRAL INSIDE A MATRIX STARTING WITH POS 0 0"""
def give_values(list_, m):
    matrix2 = list()
    for x in range(m):
        matrix2 = []
        for y in range(m):
            matrix2.append(0)
        list_.append(matrix2)


def display_matrix(list_, m):
    for i in range(m):
        for j in range(m):
            if list_[i][j] < 10:
                print(f"{list_[i][j] : 3}", end="  ")
            elif list_[i][j] < 100:
                print(f"{list_[i][j] : 2}", end="  ")
            else:
                print(f"{list_[i][j]}", end="  ")
        print(" ")
        print(" ")


def main():
    n = int(input("the matrix N*N, n=:"))
    matrix = list()
    give_values(matrix, n)
    m = n * n
    n_max = n
    n_min = 0
    x = 0
    y = 0
    k = 1
    matrix[x][y] = 1
    v = 2
    while k <= m:
        while y < n_max - 1:
            y += 1
            matrix[x][y] = v
            v += 1
        k = v
        while x < n_max - 1:
            x += 1
            matrix[x][y] = v
            v += 1
        k = v
        n_max -= 1
        while y > n_min:
            y -= 1
            matrix[x][y] = v
            v += 1
        k = v
        n_min += 1
        while x > n_min:
            x -= 1
            matrix[x][y] = v
            v += 1
        k = v
    display_matrix(matrix, n)


main()
