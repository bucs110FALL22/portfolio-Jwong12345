import time

class Animal:
  def __init__(self, name, breed):
    self.id= time.strftime("%d%m%M%S")
    self.id=id(self)
    self.name=name
    self.type=breed
    self.arrived=time.strftime("%d/%m/%Y")
    self.adopted=None
  def AdoptionDate(self):
    self.adopted=time.strftime("%d/%m/%Y")
  def __str__(self):
    str_result=f"{self.name}[{self.type}]"
    str_result+=f"\narrived:{self.arrived}"
    str_result+=f"\nadopted:{self.adopted}"
    return str_result
def main():
  a = Animal("Stealth", "Dragon")
  a.AdoptionDate()
  print(a)
main()