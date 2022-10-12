import turtle

def drawEQShape(a, num_sides=0, side_length=0):
  for i in range(num_sides):
    angle=360/num_sides
    t.forward(side_length)
    t.left(angle)
window = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
sides = int(input("how many sides do you want on your shape? "))
length = int(input("how long do you want your sides to be? "))
drawEQShape(t, sides, length)

window.exitonclick()