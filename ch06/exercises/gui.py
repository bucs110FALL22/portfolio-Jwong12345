class Player:
  def __init__(self):
    self.playernum=1
    self.powerupfire=False
    self.islarge=True
    self.issmall=False
    self.CanBreakBlock=True

class Goomba:
  def __init__(self):
    self.collisionAgainstWall=False
    self.wings=False
    self.moveleft=True
    self.moveRight=False
    self.canJump=False

class Block:
  def __init__(self):
    self.breakable=True
    self.ContainCoin=False
    self.collision=True
    self.hiddenPowerUp=False