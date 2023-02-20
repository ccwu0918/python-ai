import turtle

screen = turtle.Screen()
screen.setup(500, 400)

turtle.pensize(5)
turtle.pencolor("blue")
turtle.forward(100)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.left(90)
turtle.forward(100)

screen.exitonclick()
