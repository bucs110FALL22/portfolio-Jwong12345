class StringUtility:
  def __init__(self, string):
    self.string=string
  def __str__(self):
    return self.string
  def vowels(self):
    count= 0
    vowels = "AaEeIiOoUu"
    for chr in self.string:
      if chr in vowels:
        count += 1
    if count >= 5:
      count = "many"
      return count
    elif count < 5:
      return str(count)
  def bothEnds(self):
    if len(self.string) <= 2:
      string1 = ""
      return string1
    else:
      string1 = self.string[0]+self.string[1]+self.string[-2]+self.string[-1]
      return string1
  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    first_letter=self.string[0]
    count=0
    for chr in self.string:
      if chr in first_letter:
        count += 1
    if count <= 1:
      return self.string
    else:
      for i in range(len(self.string)+1):
        string1=self.string.replace(first_letter, "*")
        string2 = first_letter + string1[1:len(string1)+1]
      return string2
  def asciiSum(self):
    total = 0
    for i in range(len(self.string)):
      total = total + ord(self.string[i])
    return total
  def cipher(self):
    offset = len(self.string)
    new_string = ""
    if offset > 26:
      offset = offset - 26
    for i in range(len(self.string)):
      if ord(self.string[i]) == 32:
        new_string += chr(32)
      else:
        encrypt = (ord(self.string[i])+ offset)
        if encrypt > ord('z'):
          encrypt = encrypt - 26
          new_string += chr(encrypt)
        elif encrypt > 90 and encrypt in range(91,97):
          encrypt = encrypt - 26
          new_string += chr(encrypt)
        else:
          new_string+= chr(encrypt)
    return new_string