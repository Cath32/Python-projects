#
# Cathrine Bien-Aime
#
# sumNumbers.py
#
# Sum a series of numbers entered by the user
#
# Input: How many numbers to sum (n)
#        Value for the n numbers
#
# Processing: 1. Prompt user for how many numbers to sum (n)
#             2. For each of the n numbers:
#                 prompt user for the value     
#                add number to the accumulator
#             3. Display the number of the sum entered
#
# Output: Sum of n numbers
#
#

def main():
    print("Sum of Numbers...")
    print()

    n = eval(input("How many numbers do you want to sum? "))

    # Initialize accumulator
    sum = 0

    for i in range(n):
        # Prompt user for the value
        value = eval(input("\tEnter number " + str(i+1) + ": "))

        # Add number to the accumulator
        sum = sum + value

    # Display result
    print("\nThe sum of the numbers is: ", sum)

main()
    
    
