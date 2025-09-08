
def average_age():
    # Get User Input
    age1 = (input('enter age of friend 1:'))
    age1 = int(age1)
    age2 = (input('enter age of friend 2:'))
    age2 = int(age2)
    age3 = (input('enter age of friend 3:'))
    age3 = int(age3)
    age4 = (input('enter age of friend 4:'))
    age4 = int(age4)
    age5 = (input('enter age of friend 5:'))
    age5 = int(age5)
    # Sum ages
    sum = age1 + age2 + age3 + age4 + age5 
    # average the ages
    average = sum/5 
    # Print the results
    print("average age is" , average)
# Line which calls the above function.
average_age()