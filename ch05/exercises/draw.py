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

import random
import pygame

pygame.init()
screen = pygame.display.set_mode()

width, height = pygame.display.get_window_size(
)  #  returns as a tuple of 2 items (w, h)

red = [200, 0, 0]
purple = [200, 0, 200]
green = [0, 200, 0]
blue = [0, 0, 200]

bright_red = [255, 0, 0]
bright_purple = [255, 0, 255]
bright_green = [0, 255, 0]
bright_blue = [0, 0, 255]

black = [0, 0, 0]

instructions = """
    UP: red
    DOWN: purple
    LEFT: green
    RIGHT: blue
"""

msg = "Press spacebar to play the game..."
direction = ["UP", "DOWN", "LEFT", "RIGHT"]

hit_box_width = width / 3
hit_box_height = height / 3

red_button_box = pygame.Rect(0, 0, hit_box_width, hit_box_height)
purple_button_box = pygame.Rect(0, 0, hit_box_width, hit_box_height)
blue_button_box = pygame.Rect(0, 0, hit_box_width, hit_box_height)
green_button_box = pygame.Rect(0, 0, hit_box_width, hit_box_height)

green_button_box.topright = red_button_box.bottomright
blue_button_box.topleft = red_button_box.topright
purple_button_box.topleft = green_button_box.topright

red_button = pygame.draw.rect(screen, red, red_button_box)
green_button = pygame.draw.rect(screen, green, green_button_box)
blue_button = pygame.draw.rect(screen, blue, blue_button_box)
purple_button = pygame.draw.rect(screen, purple, purple_button_box)

lost = False
result = []
turns = len(direction)

#each time through the while is one frame
while not lost:
    # draw an image based on the program's current state
    # 1. respond to events
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                random.shuffle(direction)
                for i in direction:
                    if i == "UP":
                        red_button = pygame.draw.rect(screen, bright_red,
                                                      red_button_box)
                    elif i == "DOWN":
                        purple_button = pygame.draw.rect(
                            screen, bright_purple, purple_button_box)
                    elif i == "LEFT":
                        green_button = pygame.draw.rect(
                            screen, bright_green, green_button_box)
                    elif i == "RIGHT":
                        blue_button = pygame.draw.rect(screen, bright_blue,
                                                       blue_button_box)
                    pygame.display.flip()
                    pygame.time.wait(500)
                red_button = pygame.draw.rect(screen, red, red_button_box)
                green_button = pygame.draw.rect(screen, green,
                                                green_button_box)
                blue_button = pygame.draw.rect(screen, blue, blue_button_box)
                purple_button = pygame.draw.rect(screen, purple,
                                                 purple_button_box)
                msg = "Your turn..."
                turns = len(direction)
                result = []
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            turns = turns - 1
            print(mouse_click_pos)
            if red_button_box.collidepoint(mouse_click_pos):
                red_button = pygame.draw.rect(screen, bright_red,
                                              red_button_box)
                result.append("UP")
                print("UP")
            elif purple_button_box.collidepoint(mouse_click_pos):
                purple_button = pygame.draw.rect(screen, bright_purple,
                                                 purple_button_box)
                result.append("DOWN")
                print("DOWN")
            elif green_button_box.collidepoint(mouse_click_pos):
                green_button = pygame.draw.rect(screen, bright_green,
                                                green_button_box)
                result.append("LEFT")
                print("LEFT")
            elif blue_button_box.collidepoint(mouse_click_pos):
                blue_button = pygame.draw.rect(screen, bright_blue,
                                               blue_button_box)
                result.append("RIGHT")
                print("RIGHT")
    font = pygame.font.Font(None, 18)

    # 2. updating data
    if turns == 0:
        screen.fill("black")
        msg = "You entered:" + str(result)
        msg = ", and the correct pattern was: " + str(direction)
        font_object = font.render(msg, True, "white")
        screen.blit(font_object, (10, 10))
        pygame.time.wait(200)
        if result == direction:
            msg = "Yay! You won. Wanna play again, press spacebar?"
        else:
            lost = True
            msg = "Haha you lost. Try paying attention."

    font = pygame.font.Font(None, 18)
    font_object = font.render(msg, True, "orange")

    #3. draw
    screen.blit(font_object, (10, 10))

    #4. display the screen
    pygame.display.flip()