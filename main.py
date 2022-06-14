from turtle import Turtle, Screen
import random

# import colorgram
#
# colors = colorgram.extract('paint.jpg', 10)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print (rgb_colors)

# color_list = [(237, 237, 237), (236, 233, 235), (231, 236, 233), (232, 235, 238), (193, 71, 30), (173, 49, 82), (194, 159, 15), (217, 166, 74), (66, 80, 135), (148, 31, 59)]

color_list1 = ["yellow", "green", "blue", "pink", "orange", "red", "purple", "grey", "black"]
def random_color_select():
    color = random.choice(color_list1)
    return color


my_turtle = Turtle()
my_turtle.speed('fastest')



def draw_circle(color):
    my_turtle.color(color)
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.circle(10)
    my_turtle.end_fill()

def pen_up_movement():
    my_turtle.penup()
    my_turtle.fd(40)

def next_row(row_counter, add_row_distance, direction_angle):
    my_turtle.home()
    my_turtle.penup()
    my_turtle.setheading(90)
    my_turtle.fd(add_row_distance)
    my_turtle.setheading(direction_angle)

def pattern_draw(circles, rows):
    x = 0
    circle_counter = 0
    add_row_distance = 0
    direction_angle = 0
    while x < rows :
        while (circle_counter < circles):
            color = random_color_select()
            draw_circle(color)
            pen_up_movement()
            circle_counter += 1
        x += 1
        circle_counter = 0
        add_row_distance += 70
        if (direction_angle == 0):
            direction_angle == 180
        else:
            direction_angle == 0
        next_row(x, add_row_distance, direction_angle)


pattern_draw(10, 5)
screen1 = Screen()
screen1.exitonclick()