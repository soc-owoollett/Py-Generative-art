import turtle as t
import random

colors = ['#ff3624', '#ff8e24', '#ffd724', '#d0ff24', '#5bff24', '#24ff66', '#24ffba', '#24bdff', '#2457ff', '#7f24ff',
          '#cc24ff', '#ff63ea']
t.speed(0)
t.bgcolor("white")

t.penup()
t.setpos(-200,0)
t.pendown()
t.fd(400)

for i in range(200):
    t.penup()
    t.setpos(random.randint(-200,200),0)
    t.pendown()
    t.lt(90)
    t.fd(random.randint(20,200))
    t.rt(90)
    t.fd(5)
    t.lt(90)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

t.exitonclick()
