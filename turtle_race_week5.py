from time import sleep
from turtle import *
from random import randint

speed(20)
penup()
goto(-140,140)

for step in range(16):
  right(90)
  write(step)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    color("black")
    forward(10)
    
  penup()
  backward(160)
  left(90)
  forward(20)



sleep(30)
#turtle 1  
id500209345 = Turtle()
id500209345.color('blue')
id500209345.shape('turtle')
id500209345.penup()
id500209345.goto(-155, 100)
id500209345.pendown()

#turtle 2
josdin = Turtle()
josdin.color('red')
josdin.shape('turtle')
josdin.penup()
josdin.goto(-155, 70)
josdin.pendown()

#turtle 3  
orange_turtle = Turtle()
orange_turtle.color('orange')
orange_turtle.shape('turtle')
orange_turtle.penup()
orange_turtle.goto(-155, 40)
orange_turtle.pendown()

#turtle 4
purple_turtle = Turtle()
purple_turtle.color('purple')
purple_turtle.shape('turtle')
purple_turtle.penup()
purple_turtle.goto(-155, 10)
purple_turtle.pendown()

sleep(30)

#turtlerotation
for turn in range(72):
  josdin.right(5)
  josdin.forward(1.5)
  josdin.pendown()
#turtlerotation

for turn in range(72):
  
  orange_turtle.right(5)
  orange_turtle.forward(1.5)
  orange_turtle.pendown()
#turtlerotation
for turn in range(72):
  purple_turtle.right(5)
  purple_turtle.forward(1.5)
  purple_turtle.pendown()

#turtlerotation
for turn in range(72):
  id500209345.right(5)
  id500209345.forward(1.5)
  id500209345.pendown()

sleep(30)

#off to the races
for turn in range(100):
  id500209345.forward(randint(1,5))
  josdin.forward(randint(1,5))
  orange_turtle.forward(randint(1,5))
  purple_turtle.forward(randint(1,5))


  


sleep(30)