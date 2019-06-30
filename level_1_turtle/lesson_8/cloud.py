from turtle import *
def yunduo(n):
    forward(n)
    circle((2/5)*n, 180)
    right(90)
    circle((n/2),180)
    right(90)
    circle((2/5)*n,180)
yunduo(50)
done()