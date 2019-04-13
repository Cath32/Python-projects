#
# Cathrine Bien-Aime
#
# archerytarg.py
#
# Processing: Create a Graphic Window and draw:
#          1. Set background color
#          2. Point         
#          3. Circle
#         
# PLEASE DOWNLOAD GRAPHICS TO DESKTOP TO RUN PROGRAM
#
 
 
 
# Import gragic library
from graphics import *
 
def main():
    # Create a graphics window
    win = GraphWin("archerytarg", 500,500)
    # Set background color
    win.setBackground (color_rgb(66, 220, 244))
     
 
    # Point
    P = Point(300,300)
    P.draw(win)
 
     
    # Circle ( sizes and colors) with in a circle
    c = Circle(Point(250,250),125)
    c.setFill("black")
    c.draw(win)
    # Circle
    c = Circle(Point(250,250),100)
    c.setFill("blue")
    c.draw(win)
    # Circle
    c = Circle(Point(250,250),75)
    c.setFill("red")
    c.draw(win)
    # Circle
    c = Circle(Point(250,250),50)
    c.setFill("yellow")
    c.draw(win)
    # Circle
    c = Circle(Point(250,250),25)
    c.setFill("white")
    c.draw(win)
 
main()
