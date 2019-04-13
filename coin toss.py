#
# Cathrine Bien-aime
#
# CoinToss.py
#
# Simulate coin tosses as many times as indicated by the user
#
# Input: Number of times the coin will be tossed
#
# Processing: 1. Prompt user of number of times the coin will be tossed (n)
#             2. Repeat n times.
#                     Generate random number (1/2)
#                     If 1 => Heads
#                     If 2 => Tales
#
# Output: n simulations of a coin toss (Heads / Tales)
#
 
 
# Simulates a single tossing of a coin and displays Head/Tales
 
#Import random library
from random import *
def coinToss():
    # Generate random number (1/2)
    toss = randint(1,2)
 
    # Display results
    if toss ==1:
        print("\tHeads")
    else:
        print("\tTales")
 
def main():
    print("Coint Toss Game ...")
    print()
 
    # Prompt user of number of times the coin will be tossed
    n = int(input("How many times do you want to toss the coin? "))
 
    # Simulate tossing
    for i in range(n):
        coinToss()
             
     
     
main()
