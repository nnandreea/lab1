print("First task:")
x = input("First sequence:")
y = input("Second sequence:")
z = input("Third sequence:")
if x < y:
    a = x
    b = y
else:
    a = y
    b = x
if z > b:
    c = z
else:
    c = b
    if z < a:
        b = a
        a = z
    else:
        b = z
print(f"{a}, {b}, {c}")
print("Second program:")
PIN = 1234
user_input_atempt = 0
i = 0
while (i < 3) & (user_input_atempt != PIN):
    user_input_atempt = int(input("What is your pin?"))
    if user_input_atempt != PIN:
        print("Your PIN is incorrect.")
    i += 1
if i < 3:
    print("Your PIN is correct")
else:
    print("Your card is blocked")
print("third program:")
# third program
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
# primes are not necessary, it is possible to increment the number and the number between the primes wont divide exactly, in a wa
factor = 1
user_input_number = int(input("An integer: "))
i = 0
while user_input_number != 1:
    if user_input_number % primes[i] == 0:
        print(primes[i])
        user_input_number /= primes[i]
    else:
        i += 1
print("fourth program: ")
# fourth program
r_old = int(input("Enter a number: "))
A = 32310901
B = 1729
M = pow(2, 24)
print("100 random numbers:")
for x in range(100):
    r_new = (A*r_old + B) % M
    print(f"the number {x} : {r_new}")
    r_old = r_new
# fifth program
A = 0.1
B = C = 0.01
D = 0.00002
prey = 100
predator = 20
before = 20
prey = prey*(1 + A - B * predator)
before = before*(1 - C + B * prey)
print(f"prey: {prey}, predator {before}")
# use the round , because there cant be 34.52427 preys
# seventh program
NR_OF_TICKETS = 100
i = 0
while NR_OF_TICKETS > 0:
    buyer_ticket = int(input("How many tickets? "))
    if buyer_ticket > 4:
        print("Ypu can't buy more than 4 tickets")
    else:
        NR_OF_TICKETS -= buyer_ticket
        i += 1
print(f"there were {i} buyers")
