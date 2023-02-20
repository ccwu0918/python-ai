import turtle

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 7):
    turtle.forward(100)
    turtle.left(60)

screen.exitonclick()
