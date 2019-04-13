#
# Cathrine Bien-Aime
#
# Invest.py
#
# This program calculates the amount of time it takes  for  an  investment
#         to  double  at  a  given  interest  rate.
#
# Input: Number of years, Annual interest rate
#
# Output: 1. Interest rate
#         2. Years to double
# 
#
 
def main():
    # Title
    print("Number of years for an investment to double")
    print()
 
    # Prompt user for the annual interest rate
    apr = eval(input("Enter the annual interest rate: " ))
     
 
 
    # calculate
    years = 0
    investm = 10.00
    while investm < 20:
        investm =  investm *  apr
        years = years + 1 
          
         
 
    # Display result    
    print("Years to double: ", years)
 
 
 
 
 
 
main()
