#es4
BOOKS_COST = 17647
NR_OF_BOOKS = 256
SHIPPING_FEE = 2
TAXES = 0.075

Order_Price = BOOKS_COST + BOOKS_COST*TAXES + NR_OF_BOOKS*SHIPPING_FEE
print(Order_Price)
#es5
LAT_A = 15
LAT_B = 20
import math
area = LAT_A*LAT_B
perim = 2 * (LAT_B + LAT_A)
diag = sqrt(pow(LAT_B,2)+pow(LAT_A,2))
