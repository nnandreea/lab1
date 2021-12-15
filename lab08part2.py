import random
N = 4


def give_values(list_, n):
    for x in range(n):
        list_.append(random.randint(0, 100))
    return list_


def give_values2(list_, n, m):
    list_2 = list()
    for x in range(n):
        for y in range(m):
            list_2.append(random.randint(0, 100))
        list_.append(list_2)
        list_2 = []
    return list_


def check_if_magic_square(list_):
    a = 1
    general_sum = 0
    sums = list()
    for x in range(N):
        sum_ = 0
        for y in range(N):
            sum_ += list_[x][y]
        sums.append(sum_)
    i = 0
    while i < 3:
        if sums[i] == sums[i+1]:
            i += 1
        else:
            break
    if i == 0:
        a = 0
    else:
        general_sum = sums[0]
        sums = []
        for y in range(N):
            sum_ = 0
            for x in range(N):
                sum_ += list_[x][y]
            sums.append(sum_)
        i = 0
        while i < 3:
            if sums[i] == sums[i+1]:
                i += 1
            else:
                break
        if (i == 0) | (general_sum != sums[0]):
            a = 0
        else:
            sum1 = 0
            sum2 = 0
            for x in range(0, 4):
                sum1 += list_[x][x]
                sum2 += list_[3-x][x]
            if sum1 == sum2 == general_sum:
                a = 1
    return a


def merge_sorted(a, b):
    final_list = list()
    final_list.append(a[0])
    for x in range(1, len(a)):
        added_elem = a[x]
        n = len(final_list) - 1
        final_list.append(0)
        while (n > -1) & (added_elem < final_list[n]):
            final_list[n+1] = final_list[n]
            n -= 1
        final_list[n+1] = added_elem
    for x in range(len(b)):
        added_elem = b[x]
        n = len(final_list) - 1
        final_list.append(0)
        while (n > -1) & (added_elem < final_list[n]):
            final_list[n+1] = final_list[n]
            n -= 1
        final_list[n+1] = added_elem
    return final_list


def main():
    magic_square = list()
    # magic_square = give_values2(magic_square, 4, 4)
    magic_square = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]
    print("the matrix:")
    print(magic_square)
    print("the ordered matrix:")
    for x in range(4):
        for y in range(4):
            print(magic_square[x][y], end='\t')
        print("")
    if check_if_magic_square(magic_square):
        print("the matrix is a magic square")
    else:
        print("the matrix is not a magic square")
    a = list()
    a = give_values(a, random.randint(1, 20))
    b = list()
    b = give_values(b, random.randint(1, 20))
    print(merge_sorted(a, b))


main()
