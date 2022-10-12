
def star_pyramid():
  rows =int(input("how many rows of stars do you want?"))
  t = "*"
  stars = 1
  for i in range(1,rows + 1, 1):
    print(t * stars)
    stars = stars + 1

star_pyramid()

def rstar_pyramid():
  rows =int(input("how many rows of stars do you want?"))
  t = "*"
  stars = rows
  for i in range(1,rows + 1, 1):
    print(t * stars)
    stars = stars -1
rstar_pyramid()