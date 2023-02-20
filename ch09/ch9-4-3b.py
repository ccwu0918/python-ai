import turtle

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 4):
    turtle.forward(100)
    turtle.left(120)

screen.exitonclick()
