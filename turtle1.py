import turtle
from colorsys import hsv_to_rgb

def hue2rgb(hue, saturation=1, value=0.8, rgb_scale = 1):
    return tuple(rgb_scale*c for c in hsv_to_rgb(hue, saturation, value))
color = 1/3 

var = 15
var2 = -15
wn = turtle.Screen()
mrtop = turtle.Turtle()
mrbottom = turtle.Turtle()
mrbottom.setheading(360)
mrtop.speed(10)
mrbottom.speed(10)
#print(mrtop.colormode())
#wn.bgpic("bg.jpg")


for i in range(1,12):
    color+=0.1
    mrtop.color(hue2rgb(color,0.9,0.7))
    print(mrtop.heading(),"first")
    mrtop.setheading(mrtop.heading()+1)
    var = var + 15
    mrtop.circle(var)
    
for i in range(1,12):
    color+=0.1
    mrbottom.color(hue2rgb(color,0.9,0.7))
    print(mrbottom.heading(),"second")
    mrbottom.setheading(mrbottom.heading()-1)
    var2 = var2 - 15
    mrbottom.circle(var2)

wn.exitonclick();
