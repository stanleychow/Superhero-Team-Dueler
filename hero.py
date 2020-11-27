from ability import Ability
from armor import Armor

#Random Module
import random

#Hero Constructor
class Hero():
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

#Fight Method
    def fight(self, opponent):
        heroes_list = [self.name, opponent.name]
        print(str(random.choice(heroes_list)) + " won!")

# #Grace Hopper Constructor
# if __name__  == "__main__":
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
