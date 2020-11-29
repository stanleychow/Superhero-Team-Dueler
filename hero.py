from ability import Ability
from armor import Armor
from weapon import Weapon

#Random Module
import random

#Hero Constructor
class Hero():
    def __init__(self, name, starting_health = 100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

#Add Ability Method
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()
        return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
    
    def fight(self, opponent):  
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
           print("Draw")
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive() == False:
                self.add_death(1)
                opponent.add_kill(1)
                print(f"{opponent.name} won!")
            elif opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{self.name} won!")

        

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths
       
               





# #Grace Hopper Constructor
# if __name__  == "__main__":
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

# if __name__ == "__main__":
#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")

#     hero1.fight(hero2)

# if __name__ == "__main__":
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     print(hero.abilities)

# if __name__ == "__main__":
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.attack())

# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Sheild", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.current_health)
    
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())