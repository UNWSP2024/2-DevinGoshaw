# average age of friends program
#Programmer: Devin Goshaw 
#Date: 9\9\2025


def average_age():
    # Get User Input
    age1 = (int(input('enter age of friend 1:')))
    age2 = (int(input('enter age of friend 2:')))
    age3 = (int(input('enter age of friend 3:')))
    age4 = (int(input('enter age of friend 4:')))
    age5 = (int(input('enter age of friend 5:')))
    # Sum ages
    sum = age1 + age2 + age3 + age4 + age5 
    # average the ages
    average = sum/5 
    # Print the results
    print("average age is" , average)

# Line which calls the above function.
average_age()