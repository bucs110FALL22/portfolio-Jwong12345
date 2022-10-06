import turtle
import random


window = turtle.Screen()
window.setup (width=400, height=300, startx=0, starty=0)
mike = turtle.Turtle()
mike.shape("turtle")
mike.color("blue")
mike.goto(0, 0)
mike.up()
i = True
while i is True:
  list = [1,2]
  choice = random.choice(list)
  print(choice)
  POS = []
  POS = mike.pos()
  x = mike.xcor()
  y = mike.ycor()
  print(x)
  print(y)
  if x > 300:
    break
  if x < -200:
    break
  if y < -200:
    break
  if y > 300:
    break
  if choice == 1:
    mike.left(90)
    mike.forward(50)

  if choice == 2:
    mike.right(90)
    mike.forward(50)

window.exitonclick()
