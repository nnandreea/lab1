print("First exercise:")
first_num = int(input("1st number :"))
second_num = int(input("2nd number :"))
third_num = int(input("3rd number :"))
if (first_num == second_num == third_num):
    print("the numbers are identical")
else:
    if ((first_num<=second_num)&(second_num<=third_num)):
        print("increasing")
    elif ((first_num>=second_num)&(second_num>=third_num)):
        print("decreasing")
    else:
        print("neither")

print("Second exercise:")
grade =input("your grade as a letter A B C D F with + or -: ")
num_grade = 0
if (len(grade)==2):
    if grade[1]=="+":
        num_grade+=0.3
    elif grade[1]=="-":
        num_grade-=0.3

if grade[0]=="A":
        if(num_grade > 0):
            num_grade = 4
        else:
            num_grade+=4
elif grade[0]=="B":
        num_grade+= 3
elif grade[0]=="C":
        num_grade+= 2
elif grade[0]=="D":
        num_grade+= 1
elif grade[0]=="F":
        num_grade = 0

if ((len(grade)>=2)&(grade[0]=="F")):
    print("This grade does not exist")
else:
    print(f"your grade is :",num_grade)

print("Exercise 3:")
sequence = input("input a sequence of characters: ")
n = len(sequence)
nr_of_uppers = 0
nr_of_lowers = 0
nr_of_digits = 0
for x in range(n):
    if sequence[x].isupper():
        nr_of_uppers += 1
    if sequence[x].islower():
        nr_of_lowers += 1
    if sequence[x].isdigit():
        nr_of_digits += 1
if nr_of_uppers == n:
    print("the sequence consists only of uppercase letters")
elif nr_of_lowers == n:
    print("the sequence consists only of lowercase letters")
elif nr_of_uppers + nr_of_lowers == n:
    print("the sequence consists only of letters")
elif nr_of_digits == n:
    print("the sequence consists only of numbers")
elif nr_of_uppers+nr_of_lowers+nr_of_digits == n:
    print("the sequence consists only of letters and numbers")
if sequence[0].isupper():
    print("the first character of the sequence is uppercase")
if sequence[-1] == ".":
    print("the sequence ends with a dot :)")
print("exercise 4:")
fourth_num = int(input("Which month?: "))
fifth_num = int(input("Which day?: "))
seasons = ["Winter", "Spring", "Summer", "Autumn"]
cc = fourth_num/3
snr = 0
if ((fourth_num<1)&(fourth_num>12)):
    print("The value selected for moth is not valid")
elif cc <= 1:
    snr = 0
elif (cc <= 2):
    snr = 1
elif cc <= 3:
    snr = 2
elif cc <= 4:
    snr = 3
if((fourth_num%3==0)&(fifth_num>20)):
    snr = snr + 1
    if snr == 4:
        snr = 0
print(seasons[snr])
print("Exercise 5:")
num_of_year = int(input("Input a year: "))
div1 = num_of_year % 4
div2 = num_of_year % 100
div3 = num_of_year % 400
if(((div1 == 0)&(div2!=0))|(div3==0)):
    print("This is a leap year")
else:
    print("This is not a leap year")
print("Exercise 6:")
AllGrades=["F","D","C","B","A"]
#diffr = 0.3
your_grade=float(input("What is your grade? "))
import math
if your_grade<=4:
    x = round(your_grade)
final_grade = AllGrades[x]
if your_grade<x:
    if (your_grade+0.3<=x):
        final_grade = final_grade + "-"
        print(final_grade)
else:
    if (your_grade-0.3>=x):
        final_grade = final_grade + "+"

#print(final_grade)
print("Your grade is :", final_grade)
print("Exercise 7:")
stat = input("Are you married? ")
In = int(input("Which is your income?"))
if stat == "yes":
    a = 1
elif stat == "no":
    a = 0
# a is true if married, false if not
if (a):
    if ((In>0)&(In<16000)):
        tax_fee = 0.1*In
    elif In < 64000:
        tax_fee = 0.15*In + 1600
    else:
        tax_fee = 0.25*In + 8800
else:
    if ((In>0)&(In<8000)):
        tax_fee = 0.1*In
    elif In < 32000:
        tax_fee = 0.15*In + 800
    else:
        tax_fee = 0.25*In + 4400
print("The tax fee is :", tax_fee)
print("Exercise 8:")
conv1 = ["ml", "l", "g", "kg", "mm", "cm", "m", "km"]
SI_1 = ["vol", "vol", "mass", "mass", "len", "len", "len", "len"]
conv2 = ["fl.oz", "gal", "oz", "lb", "in", "ft", "mi"]
SI_2 = ["vol", "vol", "vol", "mass", "len", "len", "len"]
unit_1 = input("Convert from? ")
a = 1
i = 0
while i < len(conv1):
    if conv1[i] == unit_1:
        break
    i += 1
if i == len(conv1):
    a = 0
    print("There is no such unit available or even existent :)")
if a:
    value_ = float(input("The value you want to convert? "))
    value_0 = value_
    unit_2 = input("Convert to? ")
    b = 1
    j = 0
    while j < len(conv2):
        if conv2[j] == unit_2:
            break
        j += 1
    if j == len(conv2):
        b = 0
        print("There is no such unit available or even existent :)")
    if b:
        if SI_1[i] != SI_2[j]:
            print("The conversion is not possible, due to incompatible values")
        else:
            if unit_1 == "ml":
                if unit_2 == "fl.oz":
                    value_ = value_ / 29.574
                elif unit_2 == "gal":
                    value_ = value_ / 3785
            elif unit_1 == "l":
                if unit_2 == "fl.oz":
                    value_ = value_ * 33.814
                elif unit_2 == "gal":
                    value_ = value_ / 3.785
            elif unit_1 == "g":
                if unit_2 == "lb":
                    value_ = value_ / 454
            elif unit_1 == "kg":
                if unit_2 == "lb":
                    value_ = value_ / 33.814   # fix the formula
            elif unit_1 == "mm":
                if unit_2 == "in":
                    value_ = value_ * 33.814  # fix the formula
                elif unit_2 == "ft":
                    value_ = value_ / 3.785  # fix the formula
                elif unit_2 == "mi":
                    value_ = value_ / 3.785  # fix the formula
            elif unit_1 == "cm":
                if unit_2 == "in":
                    value_ = value_ * 33.814  # fix the formula
                elif unit_2 == "ft":
                    value_ = value_ / 3.785  # fix the formula
                elif unit_2 == "mi":
                    value_ = value_ / 3.785  # fix the formula
            elif unit_1 == "m":
                if unit_2 == "in":
                    value_ = value_ * 33.814  # fix the formula
                elif unit_2 == "ft":
                    value_ = value_ / 3.785  # fix the formula
                elif unit_2 == "mi":
                    value_ = value_ / 3.785  # fix the formula
            elif unit_1 == "km":
                if unit_2 == "in":
                    value_ = value_ * 33.814  # fix the formula
                elif unit_2 == "ft":
                    value_ = value_ / 3.785  # fix the formula
                elif unit_2 == "mi":
                    value_ = value_ / 3.785  # fix the formula
            print(f"The conversion is : from  {value_0}  {unit_1} to {value_:.3f} {unit_2}")
            print(f"Bravo, Andreita, you are the best, you just succeeded to make an convertor. Cheers :)))")
print("Exercise 9:")
num = int(input("Money spent in the supermarket:"))
if num < 10:
    print("There is no coupon.")
else:
    if num < 60:
        cp = 0.08*num
    elif num < 150:
        cp = 0.1*num
    elif num < 210:
        cp = 0.12*num
    else:
        cp = 0.142*num
    print("The value of the coupon is: ", cp)
