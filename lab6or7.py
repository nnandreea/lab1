# lab 07 from 18 nov cs
import random


def first(numbers):
    for x in range(12):
        numbers.append(int(random.uniform(1, 100)))
    print(numbers)
    print("All elements with even index:")
    x = 0
    while x < 12:
        print(numbers[x])
        x += 2
    print("all elements with the same value:")
    for x in range(12):
        k = 0
        for j in range(x+1, 12):
            if numbers[j] == numbers[x]:
                k += 1
                if k == 1:
                    print(f" same value elem: {numbers[x]}")
                print(numbers[j])
    print("Numbers in the reversed order")
    j = 0
    while j < 6:
        a = numbers[j]
        numbers[j] = numbers[11-j]
        numbers[11-j] = a
        j += 1
    print(numbers)


def second():
    user = input(" A number?")
    a = 1
    s = 0
    while user != "":
        s = s + a*int(user)
        a = a*(-1)
        user = input(" A number?")
    print("the alternating sum:")
    return s


def sameSet(a, b):
    k = 0
    for x in a:
        for j in b:
            if x == j:
                k += 1
                break
    if k == len(a):
        print("they are the same!")


def give_values(a):
    for x in range(20):
        a.append(int(random.uniform(0, 99)))


def userInpL_(list_):
    user_input = input("A number?")
    while user_input != "":
        list_.append(int(user_input))
        user_input = input("A number?")


def local_max(list_):
    k = 0
    n = len(list_)-1
    if n > 2:
        for x in range(2, n):
            max_ = list_[x]
            if (max_ > list_[x-2]) & (max_ > list_[x-1]) & (max_ > list_[x+1]):
                print(f"local max: {max_}")
                k += 1
        if k == 0:
            print("The are no local maximums")


def sumWithoutSmallest(list_):
    min_ = list_[0]
    s = 0
    for x in list_:
        s += x
        if min_ > x:
            min_ = x
    s -= min_
    return s



def main():
    list_1 = []
    first(list_1)
    print(second())
    a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    b = [11, 11, 7, 9, 16, 4, 1]
    sameSet(a, b)
    sequence_1 = []
    give_values(sequence_1)
    print(f"the given sequence : {sequence_1}")
    sequence_1.sort()
    print(f" the sorted sequence: {sequence_1}")
    sequence_2 = []
    userInpL_(sequence_2)
    local_max(sequence_2)
    sequence_3 = []
    give_values(sequence_3)
    print(sequence_3)
    print(f"Sum without the smallest number in list: {sumWithoutSmallest(sequence_3)}")


main()
