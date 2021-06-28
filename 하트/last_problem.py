import turtle as t
import math as m

t.shape("turtle")
t.color("red")
t.speed(1)

t.begin_fill()
for x in range(100):
    h = m.pi * x / 50
    x = 160 * m.sin(h)**3
    y = 130 * m.cos(h) - 50 * m.cos(2*h) - 20 * m.cos(3*h) - 10 * m.cos(4*h)
    t.goto(x,y)
t.end_fill()
