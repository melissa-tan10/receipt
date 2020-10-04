# Melissa Tan
# September 27, 2020
# This program processes a table's order and prints out a receipt.

print("Melissa's Italian Restaurant Receipt\n")
table_order = ['Pasta Bolognese', 'Pasta Carbonara', 'Salad', 'Diet Coke', 'Sprite']
menu_prices = [10.99, 11.99, 2.99, 1.99, 1.99]
for (a, b) in zip(table_order, menu_prices):
     print (a, b)
sum = 0
for price in menu_prices:
    sum = round(sum + price, 2)
tax = round(sum * .0625, 2)
grand = round(sum * 1.0625, 2)
print("\nTotal: $", sum)
print("Tax 6.25%: $", tax)
print("Grand Total: $", grand)
print("\nThank you for dining with us! We hope to see you again!")
