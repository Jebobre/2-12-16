__author__ = 'student'
import turtle
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()

def F(l=3):
    turtle.forward(l)

def X(l=3,n=10):
    if n==0:
        return
    F(l)
    Y(l,n-1)
    turtle.left(60)
    F(l)
    X(l,n-1)
    turtle.left(60)
    F(l)
    Y(l,n-1)


def Y(l,n):
    if n==0:
        return
    F(l)
    X(l,n-1)
    turtle.right(60)
    F(l)
    Y(l,n-1)
    turtle.right(60)
    F(l)
    X(l,n-1)

turtle.speed(10000)
F();X()
turtle.mainloop()