import turtle
t=turtle.Pen()
t.shape('turtle')
t.color('blue')
t.stamp
move=30

for i in range(12):
    t.penup()
    t.fd(55)
    t.pendown()
    t.fd(20)
    t.penup()
    t.fd(15)
    t.stamp()
    t.home()
    t.right(move)
    move=move+30
