import turtle
import random


window = turtle.Screen()
window.setup(width=400, height=300, startx=0, starty=0)
mike = turtle.Turtle()
mike.shape("turtle")
mike.color("blue")
mike.goto(0, 0)
mike.speed(0)
# mike.up()
distance = 15
angle = 90
i = True
while i is True:
  list = [1,2]
  choice = random.choice(list)
  POS = []
  POS = mike.pos()
  x = mike.xcor()
  y = mike.ycor()
  if x > 200:
    window.bgcolor("yellow")
    break
  if x < -200:
    window.bgcolor("yellow")
    break
  if y < -150:
    window.bgcolor("yellow")
    break
  if y > 150:
    window.bgcolor("yellow")
    break
  if choice == 1:
    mike.left(angle)
    mike.forward(distance)

  if choice == 2:
    mike.right(angle)
    mike.forward(distance)

window.exitonclick()
