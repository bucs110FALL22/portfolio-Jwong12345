import random 
import math
import pygame
pygame.init()
screen = [200,200]
width = 200
height = 200
window = pygame.display.set_mode(screen)
distance_from_center = [(100,100)]
hit_box_width = 100
hit_box_height = 100
red_button_box = pygame.Rect(0, 0, hit_box_width, hit_box_height)
green_button_box = pygame.Rect(0, 0, hit_box_width, hit_box_height)
x2 = 100
y2 = 100
i = True
red = [220, 0, 0]
green = [0, 220, 0]
bright_red = [255, 0, 0]
bright_green = [0, 255, 0]
color = "blue"
color2 = "black"
color3 = "red"
color4 = "green"
window.fill("white")
pygame.draw.circle(window, color, (100, 100), 100)
pygame.draw.line(window, color2, (0, 100), (200, 100))
pygame.draw.line(window, color2, (100, 0), (100, 200))
pygame.display.flip()
green_button_box.topleft = red_button_box.topright
red_button = pygame.draw.rect(window, red, red_button_box)
green_button = pygame.draw.rect(window, green, green_button_box)
pygame.display.flip()
score1=0
score2=0
print("Guess who wins the dart game")
while i is True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if red_button_box.collidepoint(mouse_click_pos):
              print("you selected player 1")
              red_button = pygame.draw.rect(window, bright_red,
                                              red_button_box)
              pygame.display.flip()
              choice = "red"
              i = False
            elif green_button_box.collidepoint(mouse_click_pos):
              print("you selected player 2")
              green_button = pygame.draw.rect(window, bright_green,
                                                 green_button_box)
              pygame.display.flip()
              choice = "green"
              i = False
window.fill("white")
pygame.draw.circle(window, color, (100, 100), 100)
pygame.draw.line(window, color2, (0, 100), (200, 100))
pygame.draw.line(window, color2, (100, 0), (100, 200))
pygame.display.flip()
for i in range(10):
  x1= random.randrange(201)
  y1= random.randrange(201)
  pygame.draw.circle(window, color3, (x1,y1), 5)
  pygame.display.flip()
  pygame.time.wait(1000)
  distance_from_center = math.hypot(x1-x2, y1-y2)
  if distance_from_center <= width/2:
    score1 = score1 + 1
  x1= random.randrange(201)
  y1= random.randrange(201)
  pygame.draw.circle(window, color4, (x1,y1), 5)
  pygame.display.flip()
  pygame.time.wait(1000)
  distance_from_center = math.hypot(x1-x2, y1-y2)
  if distance_from_center <= width/2:
    score2 = score2 + 1
print("player 1 scored ", score1, "points")
print("player 2 scored", score2, "points")

if score1 == score2:
  print("there was a tie")
if score1 > score2:
  print("player 1 won")
  if choice == "red":
    print("You were correct")
  else:
    if choice != "red":
      print("you were wrong")
if score1 < score2:
  print("player 2 won")
  if choice == "green":
    print("You were Correct")
  else:
    if choice != "green":
      print("you were wrong")
