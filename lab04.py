import random
import math
# laboratory exercises 4
print("First program:")
count = 0
input_val = input()
min_ = int(input_val)
max_ = int(input_val)
sum_even = 0
sum_odd = 0
arr = []
while input_val != "":
    num_ = int(input_val)
    if num_ >= max_:
        max_ = num_
    if num_ <= min_:
        min_ = num_
    arr.append(num_)
    if num_ % 2 == 0:
        sum_even += num_
    else:
        sum_odd += num_
    count = count + 1
    input_val = input()
if count > 1:
    print(f"the smallest number {min_}")
    print(f"the biggest number {max_}")
    print(f"the sum of even numbers {sum_even}")
    print(f"the sum of odd numbers {sum_odd}")
    print("The cumulative totals:")
    sum__ = 0
    for x in arr:
        sum__ += x
        print(sum__)
    print("All adjacent duplicates:")
    n = len(arr)
    i = 0
    l = 0
    while i < n:
        j = i - 1
        while j >= 0:
            if arr[j] == arr[i]:
                print(arr[i], end="")
                break
            j = j - 1
        i = i + 1

else:
    print("You did not read any numbers")

print("Second program:")
sequence = input("input a sequence of characters: ")
n = len(sequence)
nr_of_letters = 0
nr_of_digits = 0
sequence_2 = ""
sequence_3 = ""
arr2 = []
vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
for x in range(n):
    if sequence[x].isupper():
        sequence_2 = sequence_2 + sequence[x]
    if sequence[x].isalpha():
        nr_of_letters += 1
        if nr_of_letters == 2:
            second_letter = sequence[x]
    if sequence[x].isdigit():
        nr_of_digits += 1
for x in range(n):
    for y in vowels:
        if sequence[x] == y:
            sequence_3 = sequence.replace(sequence[x], "_")
            arr2.append(x)
    sequence = sequence_3

print(f"only the uppercase letters in the string: {sequence_2}")
print(f"The second letter in the string: {second_letter}")
print(f"Updated new sequence without vowels: {sequence_3}")
print(f"The total number of the digits in the string: {nr_of_digits}")
print(f"The position of all vowels in the string:")
for x in arr2:
    print(x, end="")
print("Third program:")
n = int(input("Give me an integer:"))
i = 0
j = 0
print("the square:")
for i in range(0, n):
    for j in range(0, n):
        print("*", end="")
    print(" ")
print("the diamond:")
m = 2*n - 1
for i in range(0, m):
    for j in range(0, m):
        if i < n:
            c = i
        else:
            c = 2*n - i - 2
        if ((j < n-c-1)|(j > n + c - 1)):
            print(" ", end="")
        else:
            print("*", end="")
    print(" ")
print("Fourth program:")
reversible_s = input("input a sequence of characters: ")
m = len(reversible_s)
reversed_s = ""
for x in range(0, m):
    reversed_s = reversible_s[x] + reversed_s
print(f"The reversed sequence : {reversed_s}")
print("Fifth program:")
reversible_s2 = input("input a sequence of characters: ")
m = len(reversible_s2)
reversed_s2 = ""
reversed_s22 = ""
for x in range(0, m):
    reversed_s2 = reversible_s2[x] + reversed_s2
    if reversible_s2[x].isupper():
        reversed_s22 = reversible_s2[x] + reversed_s22
print(f"The reversed sequence : {reversed_s2}")
print(f"All the capital letters from last to first : {reversed_s22}")
print("Sixth program:")
x = int(input("Give me a number: "))
primes = [1]
for i in range(2, x+1):
    a = 1
    for j in range(2, i):
        if i % j == 0:
            a = 0
    if a:
        primes.append(i)
print(f"All the primes smaller than {x}:")
for y in primes:
    print(y, " ", end="")
print("Seventh program:")
input_word = input("Any word: ")
n = len(input_word)
i = 1
while i <= n:
    j = 0
    while j+i <= n:
        for x in range(j, j+i):
            print(input_word[x], end="")
        j = j + 1
        print("")
    i = i + 1
print("Eighth program")
n = int(random.uniform(10, 100))
humans_first = int(random.uniform(0, 1))
dumb_computer = int(random.uniform(0, 1))
human_wins = 0
print(f"There are {n} marbles")
if humans_first:
    print("Human has the first move")
    print(f"There are {n} marbles. You must take less than half of them, but more than 1.")
    m = int(input("How much do you take?"))
    n -= m
else:
    print("Computer has the first move")
while n > 1:
    if dumb_computer:
        x = int(random.uniform(1, n/2))
        print(f"The stupid computer took = {x}")
    else:
        z = int(math.log(n/2, 2))
        x = pow(2, z) - 1
        if x <= 0:
            x = 1
        print(f"The smart computer took = {x}")
    n = n - x
    if n == 1:
        human_wins = 0
        break
    print(f"There are {n} marbles left")
    y = int(input("How much do you take?"))
    n = n - y
    if n == 1:
        human_wins = 1
        break
if human_wins:
    print("You won!")
else:
    print("YOu lost :,(")
print(human_wins)

