#
# Cathrine Bien-Aime
#
# rectangle.py
#
# prompt the user for the width and height of a rectangle,
# calculate its area, and display the results
#

def main():
    print("geometry calculator App...")
    print()
    
    #prompt the user for the width and height
    width = eval (input("please enter rectangle's width:  "))
    height = eval (input("    \"    \"    \"     height: "))

    # calculate area
    area = width * height

    # Display results
    print("the area of a", width, "by", height, "rectangle is",
          area)

main()

    
