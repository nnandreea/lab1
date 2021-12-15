import random


def give_values(list_, n):
    for x in range(n):
        list_.append(random.randint(0, 100))
    return list_


def merge(list1, list2):
    resulting_list = list()
    a = 0
    if len(list1) < len(list2):
        n = len(list1)
        a = 1
    else:
        n = len(list2)
    for x in range(n):
        resulting_list.append(list1[x])
        resulting_list.append(list2[x])
    if a:
        m = len(list2)
        for x in range(n, m):
            resulting_list.append(list2[x])
    else:
        m = len(list1)
        for x in range(n, m):
            resulting_list.append(list1[x])

    return resulting_list


def give_values2(list_, n, m):
    list_2 = list()
    for x in range(n):
        for y in range(m):
            list_2.append(random.randint(0, 100))
        list_.append(list_2)
        list_2 = []
    return list_


def neighbour_average(values, row, column, row_max, column_max):
    average = 0
    print(f"row {row} and column {column}, coordinates of element {values[row][column]}")
    if ((row != 0) & (row != row_max)) & ((column != 0) & (column != column_max)):
        average += values[row-1][column-1]
        average += values[row-1][column]
        average += values[row-1][column+1]
        average += values[row][column-1]
        average += values[row][column+1]
        average += values[row+1][column-1]
        average += values[row+1][column]
        average += values[row+1][column+1]
        # average /= 8
    elif (row == 0) & (column == 0):
        average += values[row][column-1]
        average += values[row+1][column-1]
        average += values[row+1][column]
        # average /= 3
    elif (row == 0) & (column == column_max):
        average += values[row+1][column]
        average += values[row+1][column-1]
        average += values[row][column-1]
        # average /= 3
    elif (row == row_max) & (column == 0):
        average += values[row-1][column]
        average += values[row-1][column+1]
        average += values[row][column+1]
        # average /= 3
    elif (row == row_max) & (column == column_max):
        average += values[row-1][column]
        average += values[row-1][column-1]
        average += values[row][column-1]
        # average /= 3
    elif (row == 0) | (row == row_max):
        average += values[row][column-1]
        average += values[row][column+1]
        if row == 0:
            average += values[row+1][column+1]
            average += values[row+1][column]
            average += values[row+1][column-1]
        else:
            average += values[row-1][column+1]
            average += values[row-1][column]
            average += values[row-1][column-1]
        # average /= 5
    else:
        average += values[row-1][column]
        average += values[row+1][column]
        if column == 0:
            average += values[row+1][column+1]
            average += values[row][column+1]
            average += values[row-1][column+1]
        else:
            average += values[row+1][column-1]
            average += values[row][column-1]
            average += values[row-1][column-1]
        # average /= 5
    return average


# tic tac toe
def is_it_a_win(list_):
    winner = "winner : none"
    a = 0
    b = 0
    for x in range(3):
        k1 = 0
        k2 = 0
        for y in range(3):
            if list_[x][y] == "X":
                k1 += 1
            if list_[x][y] == "O":
                k2 += 1
        if k1 == 3:
            a = 1
        if k2 == 3:
            b = 1
    for y in range(3):
        k1 = 0
        k2 = 0
        for x in range(3):
            if list_[x][y] == "X":
                k1 += 1
            if list_[x][y] == "O":
                k2 += 1
        if k1 == 3:
            a = 1
        if k2 == 3:
            b = 1
    k1 = 0
    k2 = 0
    for x in range(3):
        if list_[x][x] == "X":
            k1 += 1
        if list_[x][x] == "O":
            k2 += 1
    if k1 == 3:
        a = 1
    if k2 == 3:
        b = 1
    k1_ = 0
    k2_ = 0
    for x in range(3):
        if list_[2-x][x] == "X":
            k1_ += 1
        if list_[2-x][x] == "O":
            k2_ += 1
    if k1_ == 3:
        a = 1
    if k2_ == 3:
        b = 1
    if a:
        winner = "player 1 won"
    if b:
        winner = "player 2 won"
    return a | b, winner


def display_board(list_):
    for x in range(3):
        for y in range(3):
            print(f"{list_[x][y]}", end='')
        print()


def main():
    n = random.randint(2, 100)
    m = random.randint(2, 100)
    a = list()
    b = list()
    a = give_values(a, n)
    b = give_values(b, m)
    print(f"first list: {a}")
    print(f"second list: {b}")
    print(f"the lists merged together{merge(a, b)}")
    n = random.randint(1, 10)
    m = random.randint(1, 10)
    print("Values for the second program  are :")
    values = list()
    values = give_values2(values, n, m)
    print(values)
    n -= 1
    m -= 1
    x = random.randint(1, n)
    y = random.randint(1, m)
    print(f"the values: {values}")
    print(f"Neighbour average for the person with the following coordinates: {x}, {y}")
    print(f"Average of the neighbours of the element {values[x][y]} : {neighbour_average(values, x, y, n, m)}")
    print("Tik Tac Toe game : ")
    print("Count the rows and columns like a person, not like a programmer ")
    tic_tac_toe = list()
    tic_tac_toe = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    a = 1
    i = 0
    while (i < 9) & a:
        if i % 2 == 0:
            print("player 1:")
            x = int(input("row?"))
            y = int(input("column?"))
            tic_tac_toe[x-1][y-1] = "X"
        else:
            print("player 2:")
            x = int(input("row?"))
            y = int(input("column?"))
            tic_tac_toe[x-1][y-1] = "O"
            print(f"{x} and {y}")
        display_board(tic_tac_toe)
        b, winner = is_it_a_win(tic_tac_toe)
        if b:
            a = 0
        i += 1
    print(winner)


main()
