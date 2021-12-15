INT_A = 1
INT_B = 2
sum_int = INT_A + INT_B
int_diff = INT_A - INT_B
int_mul = INT_A * INT_B
int_avg = (INT_A + INT_B)/2
int_dist = abs(INT_A-INT_B)
maximum = max(INT_A, INT_B)
minimum = min(INT_A, INT_B)
#the f function doesn't work in my version
#print(f"First integer is {INT_A} and second integer is {INT_B}")
#print(f"Their sum is {sum_int}")
#print(f"Their difference is {int_diff}")
#print(f"Their product is {int_mul}")
#print(f"The distance is {int_dist}")
# and so on, im way too lazy to type 3 more rows

int_a = 38164
print(int_a," is composed out of the following digits")
int1 = int_a % 10
int_a = int_a // 10
int2 = int_a % 10
int_a = int_a // 10
int3 = int_a % 10
int_a = int_a // 10
int4 = int_a % 10
int_a = int_a // 10
int5 = int_a % 10
print (int5, " ", int4, " ", int3," ", int2," ",int1)
# 3rd exercise
city_name = "Mississippi"
#gjh
sequence_1="sissi"
print(city_name.replace(sequence_1,"*****"))
modified_name = city_name[0]+city_name[1]+city_name[2]+city_name[:-3]+city_name[:-2]+city_name[:-1]
print(modified_name)
