import turtle

window = turtle.Screen()
myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.color("blue")

length = float( input("Please input how long each side should be: "))
num_sides = float( input("Please input how many sides you want: "))
angle = 360 / num_sides
for i in [angle]*num_sides
  myturtle.forward(length)
  myturtle.left(i)
window.exitonclick()