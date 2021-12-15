# p4 from lab 9
sales = list()
customers = list()
sales_ranking = list()
customers_ranking = list()
sales = [23, 45, 98, 124, 88, 12, 90, 38, 14]
customers = ["andreea", "petru", "aliona", "ion", "stefan", "dina", "andrei", "alexa", "matei"]
m = len(sales)
for x in range(m):
    customer = customers[x]
    expenses = sales[x]
    sales_ranking.append(0)
    customers_ranking.append(0)
    n = len(sales_ranking)
    while (n > 1) & (expenses > sales_ranking[n-2]):
        sales_ranking[n-1] = sales_ranking[n-2]
        customers_ranking[n-1] = customers_ranking[n-2]
        n -= 1
    sales_ranking[n-1] = expenses
    customers_ranking[n-1] = customer
print(f"ALl the customers{customers}")
print(f"Customers ranking: {customers_ranking}")
print(f"The TOP CUSTOMER of today is: {customers_ranking[0]}")
