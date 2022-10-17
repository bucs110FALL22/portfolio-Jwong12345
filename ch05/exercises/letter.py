def percentage_to_letter(score=0):
  if score >= 90:
    letter = "A"
    return letter
  elif score > 79 and score < 90:
    letter = "B"
    return letter
  elif score > 69 and score < 80:
    letter = "C"
    return letter
  elif score > 59 and score < 70:
    letter = "D"
    return letter
  elif score < 60:
    letter = "F"
    return letter

  
 
def is_passing(letter=None):
  if letter in "ABC":
    return True
  else:
    return False

score = int(input("What is your percentage grade? "))
letter = percentage_to_letter(score)
print(letter)
x = is_passing(letter)
print(x)
if x is True:
  print("you passed")
elif x is False:
  print("you failed")