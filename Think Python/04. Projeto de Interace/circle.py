import turtle
import math

t = turtle.Turtle()

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    circum = 2 * math.pi * r
    n = 50
    length = circum/n
    polygon(t, n, length)

    turtle.mainloop()

circle(t, 50)
    