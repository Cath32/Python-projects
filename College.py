#
# Cathrine Bien-Aime
#
# College.py
#
# Determine if the student is either a Freshman, Sophomore, Junior, or Senior.
#
# Input: 1. Prompt the user for the number of credits earned
#        2. Determine the students Standing
#        3. Display results
#
# Output: The students class standing
 
def main():
    print("Student College Classification ...")
    print()
 
    a = 7
    b = 16
    c = 25
    d = 26
     
    # Prompt the user for the number of credits earned
    credits = eval(input("Enter the number of credits earned:  "))
 
    # Display results
    print("The student's class standing is: ")
 
    # Determine the students Standing
    if credits <= a:
        print("Freshman")
    elif a < credits <= b:
        print("Sophomore")
    elif b < credits <= c:
        print("Junior")
    else:
        print("Senior")
     
 
 
 
   
 
main()
