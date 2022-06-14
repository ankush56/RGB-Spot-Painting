from turtle import Turtle, Screen
import random

color_list1 = ["yellow", "green", "blue", "pink", "orange", "red", "purple", "grey", "black"]
def random_color_select():
    color = random.choice(color_list1)
    return color


my_turtle = Turtle()
my_turtle.speed('fastest')
my_turtle.setheading(217)
my_turtle.penup()
my_turtle.forward(500)
my_turtle.setheading(0)

total_dots = 150
for dots in range(1, (total_dots + 1)):
    my_turtle.dot(20, random_color_select())
    my_turtle.forward(50)

# Make new line after every 15 dots
    if dots % 15 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(15 * 50)
        my_turtle.setheading(0)
my_turtle.hideturtle()
screen1 = Screen()
screen1.exitonclick()