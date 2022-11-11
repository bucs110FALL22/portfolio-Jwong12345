class StringUtility:
  def __init__(self, string):
    self.string=string
  def __str__(self):
    return self.string
  def vowels(self):
    string1= 0
    vowels = "AaEeIiOoUu"
    for vowels in self.string:
      string1 += 1
    if string1 >= 5:
      count = "many"
      return count
    elif string1 < 5:
      count = string1
      return count
  def bothEnds(self):
    if len(self.string) <= 2:
      string1 = None
      return string1
    else:
      string1 = self.string[0]+self.string[1]+self.string[-1]+self.string[-2]
      return string1
  def fixStart(self):
    first_letter=self.string[0]
    if first_letter in self.string <= 1: 
      return self.string
    for i in range(len(self.string+1)):
      string1=self.string.replace(first_letter, "*")
      string2 = first_letter + string1[1, len(string1 + 1)]
      return string2
  def asciiSum(self):
    total = 0
    for i in len(self.string+1):
      total = total + ord(self.string[i])
    return total
  def cipher(self):
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt = ""
    for i in len(self.string+1):
      encrypt += ord(self.string.index[i] + len(self.string)%27)
    return encrypt