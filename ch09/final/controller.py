import anime
import cat

class Controller:
  def __init__(self):
    self.ANIME = anime.Anime_pic(type = "", category = "")
    self.CAT = cat.Cat()
    
  def question(self):
    ANSWER = input("do you want an anime picture or a cat fact? ")
    if ANSWER == "cat fact":
      self.cat_fact()
    elif ANSWER == "anime picture":
      self.waifu_pic()
    elif ANSWER != "cat fact" or ANSWER != "anime picture":
      print("please choose one of the options.")
      self.question()
      
  def cat_fact(self):
    self.amount = int(input("how many cat facts do you want? "))
    self.CAT = cat.Cat(amount = self.amount)
    self.cat_pic = cat.Cat(amount = self.amount)
    result = self.CAT.get()
    print("here is your cat fact: ", result)
    
  def waifu_pic(self):
    self.type = input("what type do you want, sfw or nsfw? ")
    if self.type == "sfw" or self.type == "nsfw":
      pass
    elif self.type != "sfw" or self.type != "nsfw":
      print("please choose one of the types offered.")
      self.waifu_pic()
    self.ANIME.category_list()
    self.category = input("which category do you want from the list above? ")
    if self.category in self.ANIME.LIST:
      pass
    elif self.category not in self.ANIME.LIST:
      print("please choose one of the categories.")
      self.waifu_pic()
      pass
    self.ANIME = anime.Anime_pic(type = self.type, category = self.category)
    result=self.ANIME.get()
    print("here is the anime picture you asked for: ", result)