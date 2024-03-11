from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
def random_color():
    random_color = random.choice(color_bank)
    return random_color

color_bank = [ (173, 146, 146), (0, 0, 0), (254, 37, 37), (149, 56, 56), (157, 106, 106), (218, 254, 254), (254, 147, 147)]

tim = Turtle()
tim.penup()
tim.setx(-200)
tim.sety(-200)
tim.hideturtle()
for j in range(10):
    for i in range(10):
        tim.dot(20,random_color())
        tim.penup()
        tim.forward(50)
    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)



screen.exitonclick()
