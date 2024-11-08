import turtle
initial= turtle.Turtle()
initial.pensize(3)
side_length=70

#----- K
for _ in range(2):
    initial.right(90)
    initial.fd(side_length)

    initial.penup()
    initial.goto(0,0)
    initial.pendown()
    initial.right(90)
#----- K
for _ in range(2):
    initial.right(45)
    initial.fd(side_length+20)

    initial.penup()
    initial.goto(0,0)
    initial.pendown()
    initial.right(225)

#------Q
initial.penup()
initial.goto(140, 60)
initial.pendown()
initial.circle(60)

initial.penup()
initial.goto(160, -60)
initial.pendown()
initial.right(225)
initial.fd(side_length-40)
