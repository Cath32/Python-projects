#
# Cathrine Bien-aime
#
# Date.py
#
# Prompt the user for a date and parser display like meaning
#
# Input: the numerical date.
#
# Output: meaning of date

def main():

    # Prompt user for a date
    dateStr = input("please enter a date (MM/DD/YYYY): ")

    # split date into a list of MM,DD,YYYY
    dateLst = dateStr.split("/")

    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep',
              'oct','nov','dec']

    monthIdx = int(dateLst[0])-1

    # Display the date
    print("the date means: ")
    print("\tDay: " + dateLst[1])
    print("\tMonth: " + months[monthIdx])
    print("\tYear: " + dateLst[2])

    



main()
 
