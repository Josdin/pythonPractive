import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen size and color
t.pensize(3)
t.pencolor("red")

# Loop to draw 10 circles
for i in range(10):
    t.circle(i * 10)
    t.penup()
    t.right(90)
    t.forward(30)
    t.pendown()

# Hide the turtle and exit the turtle screen
t.hideturtle()
turtle.done()
