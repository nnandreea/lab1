import random

list_ = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [10, 10, 20, 20, 20, 20, 20, 20, 10, 10], [10, 10, 20, 20, 20, 20, 20, 20, 10, 10], [10, 10, 20, 20, 20, 20, 20, 20, 10, 10], [20, 20, 30, 30, 40, 40, 30, 30, 20, 20], [20, 30, 30, 40, 50, 50, 40, 30, 30, 20], [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]


def display_seats(matrix_):
    for x in range(9):
        for y in range(10):
            print(matrix_[x][y], end=" ")
        print(" ")


def main():
    display_seats(list_)
    a = 1
    while a:
        x = input("Place, Price, or exit value?")
        y = input()
        x = int(x)
        if y != "":
            y = int(y)
            if (x > 9) | (y > 10) | (x < 0) | (y < 0):
                print("the values you entered for the seat are not valid")
            else:
                if list_[x][y] == 0:
                    print("THIS SEAT IS TAKEN, TRY AGAIN")
                else:
                    list_[x][y] = 0
        elif x > -1:
            i = 0
            k1 = 1
            while (i < 9) & k1:
                j = 0
                while (j < 10) & k1:
                    if list_[i][j] == int(x):
                        k1 = 0
                        print(list_[i][j])
                    else:
                        k1 = 1
                    j += 1
                i += 1

            if (x != 10) & (x != 20) & (x != 30) & (x != 40) & (x != 50):
                print("THE PRICE YOU ENTERED IS NOT VALID")
            elif k1:
                print("Seats with this price are sold out")
            else:
                k = 1
                while k:
                    n = random.randint(0, 8)
                    m = random.randint(0, 9)
                    if list_[n][m] == x:
                        print(f"you get the following seat: line {n+1}, column {m+1}")
                        list_[n][m] = 0
                        k = 0
                    else:
                        k = 1
        else:
            a = 0
            print("!!! you entered a exit value!!!")
    display_seats(list_)


main()

