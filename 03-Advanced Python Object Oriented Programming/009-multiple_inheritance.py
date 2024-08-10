#Multiple Inheritance

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
        
    def shoot_arrow(self):
        self.num_arrows-=1
        print(f"attacking with arrows: arrows left: {self.num_arrows}")
        
    def run(self):
        print('run really fast')
        
#Multiple inheritance
class Hybridborg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
        
hb1 = Hybridborg('borgie', 50, 100)
print(hb1.attack())
print(hb1.shoot_arrow())