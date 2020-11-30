from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena():
    def __init__(self):
        self.team_one = None
        self.team_two = None
    
    def create_abilty(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?  ")
        max_damage = input("What is the max damage of the weapon?  ")
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name?  ")
        max_damage = input("What is the max damage of the armor?  ")
        return Armor(name, max_damage)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               hero.add_ability(self.create_abilty())
           elif add_item == "2":
               hero.add_weapon(self.create_weapon())
           elif add_item == "3":
               hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_name = input("Enter a Team 1 name:")
        team_one = Team(team_name)
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            team_one.add_hero(hero)
        self.team_one = team_one
    # Now implement build_team_two
    #HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_name = input("Enter a Team 2 name:")
        team_two = Team(team_name)
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            team_two.add_hero(hero)
        self.team_two = team_two

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        team_kills_2 = 0
        team_deaths_2 = 0
        for hero in self.team_two.heroes:
            team_kills_2 += hero.kills
            team_deaths_2 += hero.deaths
        if team_deaths_2 == 0:
            team_deaths_2 = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills_2/team_deaths_2))

        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()