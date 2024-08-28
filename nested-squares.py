from turtle import *
import random

def draw_square(x,y,s):
    penup()
    goto(x-s/2,y-s/2)
    pendown()
    for i in range(4):
        fd(s)
        lt(90)

setup(500,500)
width(random.randint(1,7))
print(width)
hideturtle()
tracer(False)

noise = 5
size = 100
shrink = 15

for x in range(-500+size//2, 500, size):
    for y in range(-500+size//2, 500, size):
        draw_square(x, y, 200)

        x_off = random.uniform(-noise, noise)
        y_off = random.uniform(-noise, noise)

        for i in range(6):
            draw_square(x+i*x_off, y+i*y_off, size-i*shrink)

tracer(True)
exitonclick()
