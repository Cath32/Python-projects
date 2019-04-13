#
# Cathrine Bien-Aime
#
# 
#
# This program Calculates Exam scores and gives a grade
#
# Input: 1. Prompt the user for the Exam score
#        2. Determine the students Grade
#        3. Display results
# Output: The exam grade
#
#
#
 
def main():
    print("Exam Grader ...")
    print()
 
    a = 90
    b = 80
    c = 70
    d = 60
    f = 59
 
    # Prompt the user for the Exam score
    score = eval(input("Enter The score: "))
 
    # Display results
    print("The Grade is: ")
 
 
 
    # Determine the students Grade
    if score >= a:
        print("A")
    elif a > score >= b:
        print("B")
    elif b > score >= c:
        print("C")
    elif c > score >= d:
        print("D")
    else:
        print("F")
     

 
main()
