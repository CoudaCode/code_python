class Player:
  def __init__(self, pseudo, health, attack, weapon):   #Constructeur
    self.pseudo = pseudo
    self.health = health
    self.attack = attack

    self.weapon = weapon

    print("Bienvenue au joueur ", pseudo, "/ Point de vie: ", health, " Attack: ", attack)

  def get_pseudo(self):
    return self.pseudo
  def get_health(self):
    return self.health
  def get_attack(self):
    return self.attack

  def damage(self, damage):
    self.health -= damage

  def attack_player(self, target_player):
    target_player.damage (self.weapon.damage)
