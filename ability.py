#Random Module
import random

#Ability Constructor
class Ability:
    def __init__:(self, name, max_damage):
        self.name = name 
        self.max_damage = max.damage

    def attack(self):
        random_value = random.randit(0, self.max_damage)
        return random_value