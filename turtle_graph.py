import turtle
import random

t = turtle.Turtle()
t2 =turtle.Turtle()
t2.color('red')
t.pensize(100)
t2.pensize(100)
screen = turtle.getscreen()
#screen2 = t2.getscreen()
screen.setworldcoordinates(0,0,100,1000)
#screen2.setworldcoordinates(0,0,100,1000)
t.goto(0,0)
t2.goto(0,0)
for i in range(100):
    rand = random.randint(1,1000)
    rand2= random.randint(1,1000)
    t.goto(i,rand)
    t2.goto(i, rand2)
screen.exitonclick()

    
