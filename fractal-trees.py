from turtle import *
import random

def grow(length, decrease, angle, noise=0):

    if length > 10:

        fd(length)

        new_length = length * decrease
        if noise > 0:
            new_length *= random.uniform(0.9, 1.1)

        angle_l = angle + random.gauss(0, noise)
        angle_r = angle + random.gauss(0, noise)

        left(angle_l)
        grow(new_length, decrease, angle, noise)
        right(angle_l)

        right(angle_r)
        grow(new_length, decrease, angle, noise)
        left(angle_r)

        bk(length)

pen_colours = ["#5a8c29", "#43cc48", "#1b6e2c", "#8cd660"]
bg_colours = ["#878bd4", "#95decf", "#ebe06c", "#fcdf88"]

pencolor(random.choice(pen_colours))
bgcolor(random.choice(bg_colours))
width(random.randint(1, 4))

speed(0)
tracer(False)
hideturtle()
# Tree 1------------------
penup()
goto(random.randint(-350,-200), -250)
pendown()
left(90)
grow(50, 0.8, 20, 10)

# Tree 2 -----------------
penup()
goto(random.randint(-100,200), -250)
pendown()
grow(100, 0.8, 20, 10)

# Tree 3 -----------------
penup()
goto(random.randint(200,550), -250)
pendown()
grow(60, 0.8, 20, 10)


tracer(True)
exitonclick()
