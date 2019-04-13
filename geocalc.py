# Cathrine Bien-Aime
#
# geoCalculator.py 
#
# Menu driven interface program that allows the user to calculate
# the area of either, a circle, rectangle, or a triangle.
#
# Input: 
#
# Processing: 
#
# Output:
#
#
 
 
# Libraries
import math
 
def main():
    #Initialize sentinel
    choice = 0
 
    # Test sentinel
    while choice != 4:
        # Display Menu
        print("\nGeometry Calculator ...\n")
 
        print("\t1. Calculate the Area of a Circle")
        print("\t2. Calculate the Area of a Rectangle")
        print("\t3. Calculate the Area of a Triangle")
        print("\t4. Quit")
        print()
        choice = int(input("Enter your choice (1-4): "))
 
        # Drive choice
        if choice == 1: # circle
            radius = float(input("Enter radius of circle: " ))
 
            # Promt for radius
            while radius < 0:
                print("Error ... Invalid radius. Try again")
                radius = float(input("Enter radius of circle: " ))
 
            # Calculator area
            area = math.pi * radius**2
 
            # Display the result
            print("The area of the circle is", area)
 
        elif choice ==2: # Rectangle
            # Prompt user for length & width
            length, width = eval(input("Enter length & width of rectangle" +
                                        " (seperated by comma) : "))
 
            while length < 0 or width < 0:
                print ("Error ... Invalid length/width. Try again")
                length, width = eval(input("Enter length & width of rectangle" +
                                        " (seperated by comma) : "))
 
            # calculate area
            area = length * width
 
            # Display result
            print("The area of the rectangle is", area)
 
 
        elif choice == 3: # Triangle
            # Prompt user for base & height
            base, height = eval(input("Enter base & height of Triangle" +
                                        " (seperated by comma) : "))
 
            while base < 0 or height < 0:
                print ("Error ... Invalid base/height. Try again")
                length, width = eval(input("Enter base & height of Triangle" +
                                        " (seperated by comma) : "))
 
            # calculate area
            area = base * height / 2
 
            # Display result
            print("The area of the Triangle is", area)
 
 
        elif choice == 4:
            print("\nGood Bye ... ")
 
        else:
            print("\n\tError ... Invalid choice. Tray again")
 
             
 
main()
