from player import Player
from weapon import Weapon


knife = Weapon("Couteau", 3)




player1 = Player("Diara", 30, 40, knife)
player2 = Player("Bob", 10, 20, knife)
player1.attack_player(player2)
print(player1.get_pseudo(), " attaque ", player2.get_pseudo())

print("Bienvenue au joueur ", player1.get_pseudo(), " / Point de vie: ", player1.get_health(), " / Attack: ", player1.get_attack())

print("Bienvenue au joueur ", player2.get_pseudo(), " / Point de vie: ", player2.get_health(), " / Attack: ", player2.get_attack())

