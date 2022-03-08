from random import randint
from player import Player
from computer import Computer

# PRÉSENTATION

print("Bienvenue dans Combattants de Rue LVIII 🕹")
player_name = input("Choisissez votre pseudo : ")

player = Player(player_name, 100, 3)
computer = Computer('Blanka', 100)

print(f"Ok {player.get_name().upper()} let's fight ! 🔥\n{computer.get_name().upper()} sera votre adversaire 👹")
print("=" * 40)

# FIGHT ⚔️

while True:
  player_choice = ""
  while player_choice not in ["1", "2"]:
    player_choice = input(f"Tape sur 1 pour attaquer 🤺 ou 2 si tu souhaites prendre un soin 💊 ? ({player.get_pilule()} 💊 restantes)")

  if player_choice == "1":
    player_attack = randint(5, 45)
    updated_hp = computer.get_hp() - player_attack
    computer.set_hp(updated_hp)
    print(f"Vous infligez {player_attack} points de dégâts sur votre adversaire 😱")
  elif player_choice == "2":
    if player.get_pilule() > 0:
      player_bonus = randint(10, 50)
      updated_hp = player.get_hp() + player_bonus
      player.set_hp(updated_hp)
      updated_pilule = player.get_pilule() - 1
      player.set_pilule(updated_pilule)
      print(f"Vous venez de récupérez {player_bonus} points de vie 💖\nIl vous reste {player.get_pilule()} 💊")
    else:
      print("Vous n'avez plus de potions")
      continue

  if computer.get_hp() <= 0:
    print("You win ! 🤯")
    break

  computer_attack = randint(10, 50)
  update_hp = player.get_hp() - computer_attack
  player.set_hp(update_hp)
  print(f"{computer.get_name().upper()} vient de vous infliger {computer_attack} points de dégâts ...")
  print(f"{player.get_name().upper()} = {player.get_hp()} 💖\n{computer.get_name().upper()} = {computer.get_hp()} 💖")

  if player.get_hp() <= 0:
    print("Game Over ... 🥺")
    break

# FINALE

print(f"Fin de la partie ! Merci d'avoir joué {player.get_name().upper()}")