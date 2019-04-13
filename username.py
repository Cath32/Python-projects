#
# Cathrine Bien-Aime
#
# 
#
# This program reads a person’s name and computes the corresponding username.
#
# Input: user'd first and last names
#
# Processing: 1. Prompt user for first and last names.
#             2. Get first letter of the first name. (part1)
#             3. Get the first 7 letters of the last name.(part2)
#             4. Generate the user name
#                  username = part1 + part2 (all lower case)
#             5. Display the result
#
# Output: The user name
#
#
 
def main():
    print("Yser name Generator App..")
    print()
 
    # Prompt user for first and last names.
    first = input("Please enter user's first name: ")
    last = input("please enter user's last name: ")
     
    # Generate the user name
    part1 = first[0]
    part2 = last[0:7]
 
    username = part1 + part2
 
    username = username.lower()
 
    # Display the result
    print("The username is",username) 
 
 
main()
