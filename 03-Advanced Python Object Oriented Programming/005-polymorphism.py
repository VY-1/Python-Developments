#Polymorphism

class User:
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('Do nothing')
    
#inherit User    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        self.power -=1
        print(f"attacking with power: power left {self.power}")
        

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        self.num_arrows-=1
        print(f"attacking with arrows: arrows left: {self.num_arrows}")
        
#Mehtod  
def player_attack(char):
    char.attack()
    
    
wizard1 = Wizard("Mike", 60)
archer1 = Archer("Jill", 45)

# Polymorphism
player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()