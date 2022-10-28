import turtle

SCREEN = turtle.Screen()
DEDUE = turtle.Turtle()
SCREEN.bgcolor("black")
DEDUE.shape("turtle")
DEDUE.color("white")
radius=75
print("Please scroll over to the right to see the Crest of Cethleann.")
def main(turtle, radius):
  radius_2=layer_one(turtle, radius)
  radius_3=layer_two(turtle, radius_2)
  layer_three(turtle, radius_3)
def layer_one(turle, radius):
  angle = 90
  DEDUE.circle(radius, angle)
  DEDUE.circle(-radius,-angle)
  DEDUE.up()
  DEDUE.goto(20, 25)
  DEDUE.down()
  return radius
def layer_two(turle, radius):
  angle = 90
  radius = radius-20
  DEDUE.circle(radius, -angle)
  DEDUE.circle(-radius, angle)
  DEDUE.up()
  DEDUE.goto(30, 40)
  DEDUE.down()
  return radius
def layer_three(turtle, radius):
  angle = 135
  radius = radius-30
  line_distance=90
  DEDUE.circle(-radius, -angle)
  DEDUE.forward(-line_distance)
  DEDUE.right(90)
  DEDUE.forward(line_distance)
  DEDUE.circle(radius, angle)

main(DEDUE, radius)
SCREEN.exitonclick()