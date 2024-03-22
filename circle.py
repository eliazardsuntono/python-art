from turtle import *
import math

def x_direction(theta) :
    return 200*math.sin(theta)

def y_direction(theta):
    return 200*math.cos(theta)

speed(50000000)
bgcolor("black")

for i in range(6000) :
    goto(x_direction(i), y_direction(i))
    color("red")
    goto(0,0)
done()
