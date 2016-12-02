__author__ = 'student'
import turtle

def F(l=3):
    turtle.forward(l)

def X(l=3,n=10):
    if n==0:
        return
    X(l,n-1)
    turtle.right(90)
    Y(l,n-1)
    F(l)
    turtle.right(90)

def Y(l,n):
    if n==0:
        return
    turtle.left(90)
    F(l)
    X(l,n-1)
    turtle.left(90)
    Y(l,n-1)

turtle.speed(10000)
F();X()
turtle.mainloop()
