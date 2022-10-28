import turtle

screen = turtle.Screen()
dedue = turtle.Turtle()
screen.bgcolor("black")
dedue.shape("turtle")
dedue.color("white")
print("Please scroll over to the right to see the Crest of Cethleann.")
def main(turtle):
  layer_one(turtle)
  layer_two(turtle)
  layer_three(turtle)
def layer_one(turle):
  radius = 75
  angle = 90
  dedue.circle(radius, angle)
  dedue.circle(-radius,-angle)
  dedue.up()
  dedue.goto(20, 25)
  dedue.down()
def layer_two(turle):
  angle = 90
  radius = 55
  dedue.circle(radius, -angle)
  dedue.circle(-radius, angle)
  dedue.up()
  dedue.goto(30, 40)
  dedue.down()
def layer_three(turtle):
  angle = 135
  radius = 25
  dedue.circle(-radius, -angle)
  dedue.forward(-90)
  dedue.right(90)
  dedue.forward(90)
  dedue.circle(radius, angle)

main(dedue)
screen.exitonclick()