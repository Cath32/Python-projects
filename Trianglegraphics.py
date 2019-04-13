# Triangle-graphics.py
 
# Import graphics library
from graphics import *
 
def main():
    # Create underlying Graphwin and introduce app
    win = GraphWin("Draw triangle", 500, 500)
    win.setCoords(0,0,2,8)
 
    msg = Text(Point(1,1), "") # Create a blank msg outside
    msg.draw(win)
     
 
     
    while True:
        msg.setText("Click on 3 points")
        
 
        # get and display the three vertices of the triangle
        p1 = win.getMouse()
        p1.draw(win)
        p2 = win.getMouse()
        p2.draw(win)
        p3 = win.getMouse()
        p3.draw(win)
 
 
       # Create & draw triangle
        triangle = Polygon(p1,p2,p3)
        triangle.setWidth(3)
        triangle.setOutline(color_rgb(204,255,255))
        triangle.setFill(color_rgb(51,153,255))
        triangle.draw(win)
 
        # Update msg
        msg.setText(" Click to draw again")
        win.getMouse()
 
        # Undraw object on the graphic window
        p1.undraw()
        p2.undraw()
        p3.undraw()
        triangle.undraw()
 
 
     # HELLO --> you have to click 3 points on the screen to drwa the triancle,
     #it doesnt just show up on the screen
 
 
      
 
 
main()
