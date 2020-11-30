from hero import Hero
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                print(name, hero.name)
                self.heroes.remove(hero)
                foundHero = True
                
        if not foundHero:
            return 0 
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths = 1
                kd = hero.kills / hero.deaths
                print("{}Kill/Deaths:{}".format(hero.name, kd))
            else:
                kd = hero.kills / hero.deaths
                print("{}Kill/Deaths:{}".format(hero.name, kd))

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()
        
        for hero in self.heroes:
            living_heroes.append(hero)
        
        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)
            random_hero.fight(random_opponent)
            if random_hero.is_alive() == True:
                living_opponents.remove(random_opponent)
            elif random_opponent.is_alive() == True:
                living_heroes.remove(random_hero)
