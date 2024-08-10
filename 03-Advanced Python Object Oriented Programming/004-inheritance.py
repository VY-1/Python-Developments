#Inheritance


class User:
    def sign_in(self):
        print('logged in')
    
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
        

wizard1 = Wizard("Mike", 50)
archer1 = Archer("Jill", 35)

wizard1.attack()
archer1.attack()

wizard1
print(wizard1.sign_in())

print("=======Instance of=======")

#instance of a class
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
