from random import *
from turtle import *
from varables import *
player = Turtle()
player.penup()
def forward():
	player.forward(customforward)
def backward():
	player.backward(custombackward)
def right():
	player.right(customright)
def left():
	player.left(customleft)

print("It's a " + choice(["potato", "tomato", "chicken", "SUPER POTATO"])
penup()
goto(randint(1, 100), randint(1, 100))
screen = Screen()
screen.setup(800, 560)
screen.setworldcoordinates(0, 0, 800, 560)
screen.listen()
goto(randint(1, 100), randint(1, 100))
screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(right, 'a')
screen.onkey(left, 'd')
