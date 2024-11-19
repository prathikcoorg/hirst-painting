# import colorgram
#
#
# rgb_colors =[]
# colors = colorgram.extract('hirst_image.jpg',30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.r
#    b = color.rgb.r
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import turtle as t
import random
from turtle import Screen


turtle.colormode(255)
timmy = t.Turtle()
color_list = [(125, 200, 75),(240, 130, 60),(50, 180, 220),(90, 60, 200),(255, 150, 90),(10, 90, 170),(180, 70, 255),(30, 240, 110),(200, 100, 40),(60, 160, 255),(255, 45, 75),(90, 250, 50),(170, 110, 190),(80, 50, 240),(245, 130, 35),(30, 75, 160),(120, 220, 190),(65, 180, 80),(230, 50, 120),(140, 245, 100),(15, 200, 155),(85, 135, 210),(195, 75, 135),(55, 210, 180),(250, 165, 70),(115, 45, 225),(25, 180, 140),(200, 135, 250),(70, 100, 240),(180, 240, 85)]

timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
timmy.setheading(225)
# timmy.penup()
timmy.forward(300)
timmy.setheading(0)
num_of_dots = 100

for dot_count in range(1,num_of_dots +1):
    timmy.dot(20,random.choice(color_list))
    timmy.forward(50)
    # timmy.penup()

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)



screen = Screen()
screen.exitonclick()
