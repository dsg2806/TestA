import turtle
from colorsys import hsv_to_rgb
#"Import" calls for the library called turtle and hsv_to_rgb so that certain sections of code can be used in this code.

wn = turtle.Screen()
#.Screen() initialises the screen and opens the window for use.

kermanNW = turtle.Turtle()
kermanNE = turtle.Turtle()
kermanSE = turtle.Turtle() 
kermanSW = turtle.Turtle()
#The above 4 lines of code create four turtles which are labelled for each corner they cover (NESW).

kermansquare= turtle.Turtle()
#The above turtle will be used to set the background colour later.

turtle.delay(0)
#This line speeds up the drawing speed in the code.

def bgdraw(): #This function draws the square that will be used to set the background black. 
    kermansquare.speed(0)
    kermansquare.goto(-1000,-1000)
    kermansquare.begin_fill()
    kermansquare.goto(1000,-1000)
    kermansquare.goto(1000,1000)
    kermansquare.goto(-1000,1000)
    kermansquare.goto(-1000,-1000)
    kermansquare.end_fill()
bgdraw() #This runs the function.


def hue2rgb(hue, saturation=1, value=0.8, rgb_scale = 1): #This function is required in order to make the colour work. Was provided by Dr McIver.
    return tuple(rgb_scale*c for c in hsv_to_rgb(hue, saturation, value))

def define(): #This function goes through all the initialisation of the turtles and variables such as positioning, heading, etc.
    kermanNE.penup()
    kermanNW.penup()
    kermanSE.penup()
    kermanSW.penup()
    color = 1/3
    kermanNW.setpos(-100,0)
    kermanNE.setpos(100,0)
    kermanSE.setpos(0,100)
    kermanSW.setpos(0,-100)
    kermanNW.pendown()
    kermanNW.speed(0)
    kermanNW.width(2)
    kermanNE.pendown()
    kermanNE.speed(0)
    kermanNE.width(2)
    kermanSE.pendown()
    kermanSE.speed(0)
    kermanSE.width(2)
    kermanSW.pendown()
    kermanSW.speed(0)
    kermanSW.width(2)
    kermanNW.setheading(45)
    kermanNE.setheading(225)
    kermanSE.setheading(295)
    kermanSW.setheading(125)
define()

def startrail(t, steps): #This function draws the NW star trail.
    color = 1/3
    for i in range(1,9):
        t.penup()
  
        for i in range(1, 11):
        
            color += 0.1
            t.color(hue2rgb(color,0.9,0.7))
            t.pendown()
            t.right(135)
            t.forward(steps)
            t.left(170)
            t.forward(steps)
        t.penup()
        t.setheading(t.heading() -15)
        t.backward(60)

startrail(kermanNW,30)
startrail(kermanNE,30)
startrail(kermanSE,30)
startrail(kermanSW,30)
#The above 4 lines run the functions and the main drawing part.

kermanNW.ht()
kermanNE.ht()
kermanSE.ht()
kermanSW.ht()
#The above 4 lines hide the turtle afterwards.

wn.exitonclick()
#The above line allows the window to be closed when clicked.


''' *BIN* Unused but still written code is below:
def kermanNWf(): #This function draws the NW star trail.
    color = 1/3
    for i in range(1,9):
        kermanNW.penup()
  
        for i in range(1, 11):
        
            color += 0.1
            kermanNW.color(hue2rgb(color,0.9,0.7))
            kermanNW.pendown()
            kermanNW.right(135)
            kermanNW.forward(30)
            kermanNW.left(170)
            kermanNW.forward(30)
        kermanNW.penup()
        kermanNW.setheading(kermanNW.heading() -15)
        kermanNW.backward(60)

def kermanNEf(): #This function draws the NE star trail.
   
    color = 1/3
    for i in range(1,9):
        kermanNE.penup()
  
        for i in range(1, 11):
        
            color += 0.1
            kermanNE.color(hue2rgb(color,0.9,0.7))
            kermanNE.pendown()
            kermanNE.right(135)
            kermanNE.forward(-30)
            kermanNE.left(170)
            kermanNE.forward(-30)
        kermanNE.penup()
        kermanNE.setheading(kermanNE.heading() - 15)
        kermanNE.forward(60)


def kermanSEf(): #This function draws the SE star trail.
    
    color = 1/3
    for i in range(1,9):
        kermanNW.penup()
  
        for i in range(1, 11):
        
            color += 0.1
            kermanSE.color(hue2rgb(color,0.9,0.7))
            kermanSE.pendown()
            kermanSE.right(135)
            kermanSE.forward(30)
            kermanSE.left(170)
            kermanSE.forward(30)
        kermanSE.penup()
        kermanSE.setheading(kermanSE.heading() -15)
        kermanSE.backward(60)

def kermanSWf(): #This function draws the SW star trail.
    
    color = 1/3
    for i in range(1,9):
        kermanSW.penup()
  
        for i in range(1, 11):
        
            color += 0.1
            kermanSW.color(hue2rgb(color,0.9,0.7))
            kermanSW.pendown()
            kermanSW.right(135)
            kermanSW.forward(30)
            kermanSW.left(170)
            kermanSW.forward(30)
        kermanSW.penup()
        kermanSW.setheading(kermanSW.heading() -15)
        kermanSW.backward(60)
        



kermanNWf()
kermanNEf()
kermanSEf()
kermanSWf()
'''
