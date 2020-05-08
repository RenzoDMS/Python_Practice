import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
a=210
b=280
rotar_0=0
tess.left(90)
tess.up()                     # this is new

for i in range(1,61):    # start with size = 5 and grow by 2
    teta=(2*math.pi)*(i/60)
    alfa=math.atan(b**2/(math.tan(teta)*a**2))
    r=math.sqrt(1/((math.cos(teta))**2/a**2 + (math.sin(teta))**2/b**2))
    rotar_0=abs(abs(alfa)-abs(rotar_0))
    #print(rotar_0)
    x=r*math.cos(teta)
    y=r*math.sin(teta)
    #print(x)
    tess.left(rotar_0)              # and turn her
    tess.goto(x,y)          # Move the turtle to position x,y
    tess.stamp()                # leave an impression on the canvas
    
    
wn.exitonclick()
