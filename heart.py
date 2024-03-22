from turtle import *
import math

screen = Screen()
screen.title("Heart :)")
bgcolor("black")
speed(2000)
colors = ["red", "pink"]


def x_direction(theta):
    return 15 * math.sin(theta)**3

def y_direction(theta):
    return 15 * math.cos(theta) - 5 * math.cos(2*theta) - 2 *math.cos(3 * theta)

for i in range(6000):
    goto(20 * x_direction(i), 20 * y_direction(i))
    if i % 2 == 0:
        color(colors[0])
    else:
        color(colors[1])
    goto(0,0)

for i in range(6000):
    goto(20 * x_direction(i), 20 * y_direction(i))
    if i % 2 == 0:
        color(colors[1])
    else:
        color(colors[0])
    goto(0,0)
done()