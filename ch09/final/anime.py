import requests

class Anime_pic:
  def __init__(self, type = "sfw", category = "waifu"):
    self.URL= f'https://api.waifu.pics/{type}/{category}'
    self.LIST = ["waifu", "neko", "nom", "cuddle", "cry", "awoo", "slap", "poke"]
  def category_list(self):
    print(self.LIST)
  def get(self):
    self.RESPONSE = requests.get(self.URL)
    self.INFO = self.RESPONSE.json()
    return self.INFO['url']