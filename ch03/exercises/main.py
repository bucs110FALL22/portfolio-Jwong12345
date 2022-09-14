import random
my_list = [1,2,3,4,5,6,7,8,9,10]
num = random.choice(my_list)
for i in range(3):
  ans = int(input("Please choose a number between 1 and 10: "))
  if ans > num:
    print("too low")
  if ans < num:
    print("too much")
  if ans == num:
    print("You are correct")