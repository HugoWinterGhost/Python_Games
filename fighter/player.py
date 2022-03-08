class Player:

  def __init__(self, name, hp, pilule):
    self.name = name
    self.hp = hp
    self.pilule = pilule

  def get_name(self):
    return self.name

  def set_name(self, name):
    self.name = name

  def get_hp(self):
    return self.hp

  def set_hp(self, hp):
    self.hp = hp

  def get_pilule(self):
    return self.pilule

  def set_pilule(self, pilule):
    self.pilule = pilule