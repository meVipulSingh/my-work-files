import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
t.speed(0)
c = 0
d = 0
while True:

    for i in range(4):
     t.fd(80)
     t.rt(90)
    t.rt(5)
    c +=1

    if c>= 390/5:
        t.fd(50)
        c = 0
        d += 1
        if d>+12:
           break

t.hideturtle()
turtle.done()



