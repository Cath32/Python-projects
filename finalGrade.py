#
# Cathrine Bien-Aime
#
# finalGrade.py
#
# Calculates a student's final grade for a class
#
# Input: Student Id and name
#        Grades for midterm, final and project
#
# Processing: 1. Prompt the user for student Id & name
#             2. Prompt the user for midterm, final & project grades
#             3. Calculate final grade
#                  finalGrade = (midterm + final + project) /3
#             4. Display final grade
#
# Output: Final grade
#

def main():
    # Prompt the user for personal data & grades
    print("Please enter the following data ...")
    studentId = input("\tStudent Id: ")
    studentName = input("\tStudent Name: ")
    midterm, final = eval(input("\tMidterm and Final Exam Grades (seperateed by comma): "))
    project = eval(input("\tProject Grade: "))

    # Calculate final grade
    finalGrade = (midterm + final + project) /3

    # Display result
    print()
    print("Final Grade:",finalGrade)

main()
    
