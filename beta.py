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
type = choice(["potato", "tomato", "chicken", "SUPER POTATO"])
print("It's a " + type)
if type == "tomato":
	# registering the image 
	# as a new shape 
	register_shape('tomato.gif') 
  
# setting the image as cursor 
	shape('tomato.gif') 
elif type == "potato":
	# registering the image 
# as a new shape 
	register_shape('potato.gif') 
  
# setting the image as cursor 
	shape('potato.gif') 
elif type == "chicken":
	# registering the image 
# as a new shape 
	register_shape('chicken.gif') 
elif type == "SUPER POTATO":
	# registering the image 
# as a new shape 
	register_shape('superpotato.gif') 
  
# setting the image as cursor 
	shape('superpotato.gif') 
  
# setting the image as cursor 
	shape('chicken.gif') 
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
