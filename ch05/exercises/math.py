def multiplication(num, num1):
  result=0
  for i in range(num1):
    result = result + num
  
  return result

def exponet(number, number1):
  result1=1
  for i in range(number1):
    result1 = result1*number
  return result1
def square(num1):
  res = multiplication(num1, num1)
  return res

def main():
  x = multiplication(5, 2)
  print(x)
  y = exponet(10, 2)
  print(y)
  z = square(3)
  print(z)

main()