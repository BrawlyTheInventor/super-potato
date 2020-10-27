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

print("It's a " + choice(["potato", "tomato", "chicken", "SUPER POTATO"]))
penup()
goto(randint(1, 10000000), randint(1, 10000000))
screen = Screen()
screen.setup(800, 560)
screen.setworldcoordinates(0, 0, 800, 560)
screen.listen()
screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(right, 'a')
screen.onkey(left, 'd')
while True:
	penup()
	goto(randint(1, 100), randint(1, 100))

