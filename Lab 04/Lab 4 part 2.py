import turtle 
#-------------------------- Teenage Mutant Function Turtles
#-------------------------- 2.1.1 DrawSquare

def drawSquare(myTurtle, squareSize):
    for side in range(4):
        myTurtle.forward(squareSize)
        myTurtle.right(90)

bob = turtle.Turtle()
bob.speed(0)
#drawSquare(bob, 100)

#--------------------------2.1.2 Drawing a Row of Squares
def drawRow(myTurtle, length, squareSize):
    for squares in range(length):
        drawSquare(myTurtle,squareSize)
        myTurtle.fd(squareSize)

bob = turtle.Turtle()
bob.penup()
bob.goto(0,50)
bob.pendown()
bob.speed(0)
#drawRow(bob,5, 50)
#--------------------------2.1.3 Drawing a Grid
def drawGrid(myTurtle, size, squareSize):
    for row in range(size):
        drawRow(myTurtle, size, squareSize)
        bob.backward(size * squareSize)
        bob.right(90)
        bob.forward(squareSize)
        bob.left(90)
        
bob = turtle.Turtle()
bob.penup()
bob.goto(-300,50)
bob.pendown()
bob.speed(0)
#drawGrid(bob,5, 50)
#--------------------------2.1.4 Drawing a Stair of Squares
def drawSquareStairs(myTurtle, height, squareSize):
    for h in range(1, height+1):
        drawRow(myTurtle, h, squareSize)
        bob.backward(h * squareSize)
        bob.right(90)
        bob.forward(squareSize)
        bob.left(90)

bob = turtle.Turtle()
bob.penup()
bob.goto(-300,300)
bob.pendown()
bob.speed(0)
drawSquareStairs(bob,5, 50)
    
#-------------------------- 2.2 Spirals: 2.2.1 N Sided Polygon
def drawNgon(myTurtle, numSides, sideLength):
    angle = 360/numSides
    for i in range(numSides):
        bob.fd(sideLength)
        bob.rt(angle)

bob = turtle.Turtle()
bob.penup()
bob.goto(0,300)
bob.pendown()
bob.speed(0)
#drawNgon(bob,6,100)
  #-------------------------- 2.2.2 Super Spiral
def drawNgonSpiral(myTurtle,numSides, sideLength ,numShapes):
    for j in range(numShapes):
        angle = 360/numSides
        for i in range(numSides):
              bob.fd(sideLength)
              bob.rt(angle)
        bob.rt(360/numShapes)

bob = turtle.Turtle()
bob.penup()
bob.goto(350,300)
bob.pendown()
bob.speed(0)
#drawNgonSpiral(bob,6,100,35)

#-------------------------- 3.3 Super Duper Spira
def drawNgonSuperSpiral(myTurtle,numSides, sideLength ,numShapes):
    for j in range(numShapes):
        angle = 360/numSides
        for i in range(numSides):
              bob.fd(sideLength)
              bob.pencolor("red")
              bob.rt(angle)
              bob.pencolor("blue")
        bob.rt(360/numShapes)
        bob.pencolor("green")

bob = turtle.Turtle()
bob.penup()
bob.goto(-400,300)
bob.pendown()
bob.speed(0)
drawNgonSuperSpiral(bob,6,100,35)
