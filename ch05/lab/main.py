import pygame

pygame.init()
screen_width=300
screen_height = 300
size = 25
screen = pygame.display.set_mode([screen_width, screen_height])
screen_new = pygame.transform.flip(screen, False, True)
screen.fill([0, 255,0])
pygame.display.flip()
iters={}
iters1={}
upper_limit=20
color= "black"
scale = 10
font = pygame.font.Font(None, size)
pos = (10,10)
max_value=0
max_value1=0
font = pygame.font.Font(None, size)

def sequence(n=0):
  count = 0
  while True:
    if n == 1:
      break
    elif n % 2 == 0:
      n = n//2
      count = count +1
    elif n % 2 != 0:
      n = (n*3)+1
      count = count+1
  return count
for i in range(2, upper_limit+1):
  count=sequence(i)
  iters.update({i:count})
  iters[i]=count
  iters1[i*scale]=screen_height-count*scale
  coords = list(iters1.items())
  if len(coords) > 1:
    pygame.draw.lines(screen,color , False, coords)
    pygame.time.wait(1000)
    pygame.display.update()
  if count > max_value:
    max_value = count
    max_value1= str(max_value)
    screen.fill("green")
    msg = font.render("current highest iteration is " +max_value1, True, color)
    screen.blit(msg, (0,0))
    pygame.time.wait(500)
    pygame.display.update()

  
    
