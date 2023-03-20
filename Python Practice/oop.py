# Classes
class PartyAnimal:
    x = 0
    
    def __init__(self):
        print('I am constructed')
    
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
        
    def __del__(self):
        print("I am destructed", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

# dir() and type(), dir shows classes object has, type shows class object belongs to
print(type(an))
print(dir(an))

an = 42
print('an contains', an)

# Inheritance
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.x, "points", self.points)
        
j = FootballFan()
j.party()
j.touchdown()
