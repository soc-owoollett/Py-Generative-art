import turtle as t

import random


def euler_curve(step_size, angle_step, n_steps):
    angle = 0
    for i in range(n_steps):
        t.right(angle)
        t.fd(step_size)
        angle += angle_step
        t.lt(90)


def spiral(step_size, angle_step, n_steps):
    angle = 0
    for i in range(n_steps):
        t.right(angle)
        t.fd(step_size)
        angle += angle_step


t.tracer(False)
t.bgcolor('black')
t.hideturtle()
t.speed(0)


colours = ["light blue", "purple", "yellow", "orange", "pink"]
t.pencolor(random.choice(colours))
euler_curve(random.randint(2,30), 2.73, random.randint(300,4000))


t.tracer(True)
t.exitonclick()
