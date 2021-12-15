# lab 06, 11 nov


def count_vowels(a):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    k = 0
    for j in range(0, len(a)):
        for x in vowels:
            if x == a[j]:
                k += 1
    return k


def count_words(a):
    x = 1
    j = 0
    while j < len(a):
        b = 0
        if a[j] == " ":
            i = j
            x += 1
            while a[i] == " ":
                i += 1
                b += 1
        if b == 0:
            j += 1
        else:
            j = i
    return x


def count_words2(a):
    x = 1
    j = 0
    while j < len(a):
        b = 0
        if a[j] == " ":
            if a[j+1] != " ":
                x += 1
        j += 1
    return x


def economic_subs(income, children):
    x = 0
    if (income <= 40000) & (income >= 30000):
        if children >= 3:
            x += children*1000
    elif (income < 30000) & (income > 20000):
        if children >= 2:
            x += children*1500
    elif income <= 20000:
        x += children*2000
    return x


def main():
    a = input("A string:")
    print(f" nr of the vowels in the string: {count_vowels(a)}")
    b = input("Another string:")
    print(f"met1, nr of the word in the string: {count_words(b)}")
    print(f"met2,  nr of the word in the string: {count_words2(b)}")
    a1 = int(input("income?"))
    a2 = int(input("How many children?"))
    while (a1 != -1) & (a2 != -1):
        print(f"economic subsidity for this family {economic_subs(a1, a2)}")
        a1 = int(input("Income?"))
        a2 = int(input("How many children?"))



main()
