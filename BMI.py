#
# Cathrine Bien-Aime
#
# bmi.py
#
# Input: 1. weight in lbs
#        2. height multiplied by height
#
# Output: Determines if person is in a healthy range or not
#
#

def main():
    print("Body Mass Index Calculator ...\n")

    

    weight = eval(input("Enter your weight (in pounds): "))
    height = eval(input("Enter your height (in inches): "))

    
    #square = 0.0
    bmi = (weight * 720) / (height*height)
    
    # print(bmi)
    # square = (height*height)
    # print(square)
    print("\nYour BMI is",bmi)

    

    if bmi > g  :
        print("unhealthy")
    else:
        print("Thats in a healthy range")


main()
