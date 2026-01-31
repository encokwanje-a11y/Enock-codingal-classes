actual_cost = float(input(" please snter the actual product price: "))
sale_amount = float(input("please Enter the sale amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = {0}",format (amount))
else:
    print("No profit! ! !")
