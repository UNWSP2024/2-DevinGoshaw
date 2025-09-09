#sales tax program
#programmer: Devin Goshaw
#Date: 9\9\2025

def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item,
    item1 = (float(input('enter cost of item 1:')))
    item2 = (float(input('enter cost of item 2:')))
    item3 = (float(input('enter cost of item 3:')))
    item4 = (float(input('enter cost of item 4:')))
    item5 = (float(input('enter cost of item 5:')))
    # then displays the subtotal of the sale, 
    subtotal = item1 + item2 + item3 + item4 + item5
    print('subtotal is:' , subtotal)
    # assume the sales tax is 7 percent.
    tax = round(subtotal * 0.07,2)
    print('tax is:', tax)
    # the amount of sales tax, and the total.  
    total = subtotal + tax
    print('total is:' , total)

calculate_total_purchase()