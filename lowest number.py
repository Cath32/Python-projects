#
# Cathrine Bien-Aime
#
# Lowest.py
#
# Prompt the user for three numbers & display the lowest value
#
# Input: Three numbers
#
# Processing: 1. Prompt the user for three numbers
#             2. Determine lowest
#             3. Display result
#
# Output: Lowest of the three numbers

def main():
    print("Lowest of the three App ...")
    print()

    # Prompt the user for three numbers
    n1, n2, n3 = eval(input("Please enter three numbers (seperated by commas): "))

    # Determine lowest
    lowest = n1
    if n2 < lowest:
        lowest = n2
    if n3 < lowest:
        lowest = n3

    # Display result
    print("\nThe lowest value is", lowest)


main()
