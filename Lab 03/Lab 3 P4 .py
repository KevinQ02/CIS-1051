import turtle

sd = turtle.Turtle()

side = input("number of sides")
side = int(side)

for _ in range(side):
    sd.fd(40)
    sd.left(360/side)