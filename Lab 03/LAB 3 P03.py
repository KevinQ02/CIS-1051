Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
... initial= turtle.Turtle()
... initial.pensize(3)
... side_length=70
... 
... #----- K
... for _ in range(2):
...     initial.right(90)
...     initial.fd(side_length)
... 
...     initial.penup()
...     initial.goto(0,0)
...     initial.pendown()
...     initial.right(90)
... #----- K
... for _ in range(2):
...     initial.right(45)
...     initial.fd(side_length+20)
... 
...     initial.penup()
...     initial.goto(0,0)
...     initial.pendown()
...     initial.right(225)
... 
... #------Q
... initial.penup()
... initial.goto(140, 60)
... initial.pendown()
... initial.circle(60)
... 
... initial.penup()
... initial.goto(160, -60)
... initial.pendown()
... initial.right(225)
