__author__ = 'student'
import turtle
def draw(l,n):
    if n == 0:
        turtle.forward(l)
        return
    draw(l/3,n-1)
    turtle.left(60)
    draw(l/3,n-1)
    turtle.right(120)
    draw(l/3,n-1)
    turtle.left(60)
    draw(l/3,n-1)

turtle.speed(800)
draw(800,5)
