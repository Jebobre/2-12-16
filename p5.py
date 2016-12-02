__author__ = 'student'
import turtle
def draw(l,n):
    if n == 0:
        turtle.forward(l)
        return

    turtle.right(45)
    draw(l/2,n-1)
    turtle.left(90)
    draw(l/2,n-1)
    turtle.right(45)


turtle.speed(10000)
draw(100,5)