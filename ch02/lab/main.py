
#Part A
weeks = 16
weeks = int(weeks)
classes_per_week = 5
classes_per_week = int(classes_per_week)
tuition = 6000
tuition = int(tuition)
cost_per_week = (tuition / weeks)
cost_per_week = int(cost_per_week)
cost_per_class = (cost_per_week / classes_per_week)
cost_per_class = int(cost_per_class)
print("this is your cost per class: $", cost_per_class)
print(weeks, type(weeks))
print(classes_per_week, type(classes_per_week))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))
print(cost_per_class, type(cost_per_class))
#Part B
import random

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37.38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
rn1 = int(random.choice(mylist))
print(rn1)