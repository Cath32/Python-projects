#
# Cathrine Bien-Aime
#
# Smiley-graphics.py
#
# PLEASE DOWNLOAD GRAPHICS.py TO VIEW IMAGE
#
# Draw a smiley face on the window
#
# Import graphic library
from graphics import *

def main():
    # Create the underline window
    win = GraphWin("Smiley face...", 500,500)
    win.setCoords(0,0,10,10)

    # Draw the face
    drawFace(win, Point(5,5))

    # Draw eyes
    drawEye(win,Point(4,7))
    drawEye(win,Point(6,7))

    # drawSmile
    drawSmile(win, Point(5,2))

    # draw face (window, center)
    # draw a yellow face on window at center

def drawFace(window, center):
    face = Circle(center, 4)
    face.setFill("yellow")
    face.setWidth(15)
    face.setOutline("Black")
    face.draw(window)


# draw eye (window, center)
# draw a black eye on window at center point
def drawEye(window, center):
    eye = Circle(center, 0.5)
    eye.setFill("black")
    eye.draw(window)
    

# drawSmile (window, center):
# draw a black smile at bace point
def drawSmile (window, base):
    radius = 2
    # Determine smile center point
    x = base.getX()
    y = base.getY()

    cX = x
    cY = y + radius

    # draw circle
    circle = Circle(Point(cX,cY), radius)
    circle.setFill("yellow")
    circle.setWidth(15)
    circle.setOutline("black")
    circle.draw(window)


    # Cover top part of circle
    x1= cX - radius
    y1= cY

    x2= cX + radius
    y2= cY + radius

    cover = Rectangle(Point(x1,y1), Point(x2,y2))
    cover.setFill("Yellow")
    cover.setWidth(15)              
    cover.setOutline("yellow")
    cover.draw(window)

    



    


    








main()



