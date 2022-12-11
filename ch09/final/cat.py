import requests

class Cat:
  def __init__(self, amount = 1):
    self.URL=f'https://meowfacts.herokuapp.com/?count={amount}'
  def get(self):
    self.RESPONSE = requests.get(self.URL)
    self.INFO = self.RESPONSE.json()
    return self.INFO['data']