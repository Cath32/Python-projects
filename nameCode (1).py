#
# Cathrine Bien-Aime
#
# nameCode.py
#
# This program translates a name into a numeric code (Unicode).
#
# Input: user's name
#
# Processing: 1. Prompt user for their name.
#             2. Use a loop and the ord function to decode the name.
#             3. Display results
#
# Output:  Numerical code.

def main():
    print("Name Code App..")
    print()

    # Prompt user for their name.
    name = input("\nPlease enter your name to encode: ")
    
    sum = 0

    # Display results
    print("\nThe numerical code for your name is:", end=" ")

    # using a loop and the ord function
    for ch in name:
        sum += ord(ch)
        
    print(sum)


      
  

main()


