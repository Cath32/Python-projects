#
# Cathrine Bien-Aime
#
# Sphere.py
#
# Prompt the user for the radius of a Sphere,
# and calculate and display its area
#


import math

def main():
    print("Volume and Suface are of a Sphere")
    #prompt the user for the radius
    radius = eval(input("\nPlease enter the Sphere's radius:  "))
    
    

    # calculate area
    volume = 4/3*math.pi*radius**3
    area = 4*math.pi*radius**2
    # Rounding after two digits
    volume = (round(volume,2))
    area = (round(area,2))

    #display results
    print("\nThe volume is", volume, "cubic units")
    print("The surface area is", area, "square units")
    

main()




