#Hero Constructor
class Hero():
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

#Grace Hopper Constructor
if __name__  == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

#Fight Method
def fight(self, opponent):
    self.opponent = opponent