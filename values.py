
# Cathrine Bien-Aime
#
# values.py
#
# Given two values a&b (a<=b), displays
#   = list of values from a to b
#   = sum the values from a to b
#   = Multiplication of values from a to b
#
# Creates a list of characters that includes the values from a to b
#
# Return value: List of values as a string
#
 
 
 
 
def listValues(a,b):
    # Initialize a blank string
    valStr = ""
    # Build a string with values from a to b
    for i in range(a,b+1):
        valStr = valStr + str(i) + " "
 
    # discard last whitespace
    valStr = valStr[0:-1]
 
    # Return string of values
    return valStr
 
def sumValues(a,b):
    # Initialize accumulator
    sum = 0
 
    # add values from a to b (one step at a time)
    for n in range(a, b+1):
        sum += n
 
    # return sum
    return sum
 
def main():
    print("Playing with values")
    print()
 
    # Prompt user for two values first and last (first<=last)
    print("please enter teo values: ")
    first = int(input("\tFirst: "))
    last = int(input("\tLast: "))
 
    if first > last:
        temp = first
        first = last
        last = temp
 
    # display list of values
 
    print("From", first,"to", last, ":", end="")
    values = listValues(first,last)
    print(values)
 
    print("\n\t Sum of Values:", sumValues(first,last))
 
main()
