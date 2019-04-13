#
# Cathrine Bien-Aime
#
# pizza.py
#
# Prompt the user for the cost of square inch of pizza,
#       1. Calculate and display its area
#       2. Convert cost to integer (Whole Number)
#

import math


def main():
    print("This program computes the cost per square inch of pizza.")
    print()

    # Prompt user to enter the diameter of the pizza inches
    diameter = eval(input("please enter the diameter of the piza inches (Inches):  "))
    # Prompt user to enter the price of the pizza in dollars
    price = eval(input("please enter the price of the pizza (Dollars):  "))


    # Calculate the area
    radius =  diameter / 2
    area = math.pi*radius**2
    cost = area/price

    # Converting cost to integer
    cost = (round(cost))



    # Display results
    print("\nThe cost is",cost, "per square inch.")




    
main()
