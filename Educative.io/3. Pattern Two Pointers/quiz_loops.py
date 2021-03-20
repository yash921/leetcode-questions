#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:06:21 2020

@author: yash
"""

#c. Write a for loop which will display this set of values 2,4,6,8,10,12,14,16.
def evenNumbers(n):
    for i in range(2*n + 2):
        if i > 0 and i % 2 == 0:
            print(i, end=" ")
            
n = int(input("How many even number you want? : "))
evenNumbers(n)  # Function call


####################################################################################################

#d. Write a while which will display this set of values 16,13,10,7,4,1,-2.
def series(n):
    i = int(input("Starting Number: "))
    count = 0
    while count < n:
        print(i, end=" ")
        i -= 3
        count += 1
            
n = int(input("Series Length: "))
series(n)  # Function call

######################################################################################################

# e. Write a for loop which will print ‘Loops are fun’ three times.
def printLoop(n):
    for i in range(n):
        print("Loops are fun")
            
n = int(input("How many times you want to print 'Loops are fun': "))
printLoop(n)  # Function call
    

#######################################################################################################

# f. Write a while loop that will prompt you for four numbers. Convert the number to an integer. 
# Compute the power as power = power ** number. (Hint: set power=1 before the loop, use power = power ** number in the loop). 
# Print out the product when the loop exits.

power = 1
i = 0
while i < 4:
    number = int(input("Enter the Number: "))
    power = power ** number
    i += 1
print(power)  #This Function will only print 1 because any power of 1 will also result in 1.
    



#############################################################################################################

# g. Prompt the user to enter the number of gyros to purchase. As long as the user enters a number greater than 0,
# continue to prompt for the number of gyros purchased. Print out the total number of gyros purchased once the loop exits.
# (Hint: Use sentinel control and have a priming read and a loop read.)
while True:
    n = int(input("Enter the number of gyros to purchase: "))
    if n > 0:
        continue
    # 2- If the user enters number less than or equal to zero in step e., 
    # in the loop do not multiple the number by the product.
    # Copy the code and the output from the Python Shell.
    elif n <= 0:
        print(n)
        break



# 3-)Write a function which takes two parameters, an integer for lower limit and an integer for upper limit.  Write a while loop to print the values in the range from lower to upper in the function.Call the function and pass is 6 and 20.
def lowerAndUpperLimit(lowerLimit, upperLimit):
    i = lowerLimit + 1
    while i < upperLimit:
        print(i, end = " ")
        i += 1
lowerAndUpperLimit(6,20)

















