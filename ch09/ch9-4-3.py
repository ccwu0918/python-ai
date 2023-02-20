import turtle

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 5):
    turtle.forward(100)
    turtle.left(90)

screen.exitonclick()
