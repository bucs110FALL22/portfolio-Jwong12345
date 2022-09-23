import turtle #1. import modules
import random
import pygame
import math
# #Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.forward(random.choice(range(1,101)))
leonardo.forward(random.choice(range(1,101)))
pygame.time.wait(5000)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for i in range(10):
  michelangelo.forward(random.choice(range(11)))
  leonardo.forward(random.choice(range(11)))
  pygame.time.wait(1000)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()
# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()
coords = []
num_side=3
side_length=100
offset=100
color = "blue"
for a in range(num_side):
  theta=(2*math.pi*a/num_side)
  x=(side_length*math.cos(theta)+offset)
  y=(side_length*math.sin(theta)+offset)
  coords.append([x,y])
pygame.draw.polygon(window, color, coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")
pygame.display.flip()

num_side=4
coords = []
for b in range(num_side):
  theta=(2*math.pi*b/num_side)
  x=(side_length*math.cos(theta)+offset)
  y=(side_length*math.sin(theta)+offset)
  coords.append([x,y])
pygame.draw.polygon(window, color, coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")
pygame.display.flip()

num_side=6
coords = []
for c in range(num_side):
  theta=(2*math.pi*c/num_side)
  x=(side_length*math.cos(theta)+offset)
  y=(side_length*math.sin(theta)+offset)
  coords.append([x,y])
pygame.draw.polygon(window, color, coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")
pygame.display.flip()

num_side=9
coords = []
for d in range(num_side):
  theta=(2*math.pi*d/num_side)
  x=(side_length*math.cos(theta)+offset)
  y=(side_length*math.sin(theta)+offset)
  coords.append([x,y])
pygame.draw.polygon(window, color, coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")
pygame.display.flip()

num_side=360
coords = []
for e in range(num_side):
  theta=(2*math.pi*e/num_side)
  x=(side_length*math.cos(theta)+offset)
  y=(side_length*math.sin(theta)+offset)
  coords.append([x,y])
pygame.draw.polygon(window, color, coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")
pygame.display.flip()