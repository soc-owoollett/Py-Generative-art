import turtle as t
import random

colors = ['#ff3624', '#ff8e24', '#ffd724', '#d0ff24', '#5bff24', '#24ff66', '#24ffba', '#24bdff', '#2457ff', '#7f24ff',
          '#cc24ff', '#ff63ea']
t.speed(0)
t.bgcolor("black")

for i in range(3):
    for color in colors:
        t.pencolor(color)
        t.circle(100)
        t.rt(10)


t.pencolor("white")
t.speed(0)

for i in range(4):
    for i in range(90):
        t.fd(4)
        t.rt(4)
    t.lt(90)


t.exitonclick()
