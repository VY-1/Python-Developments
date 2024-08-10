# @classmethod and @staticmethod

class PlayerCharacter:
    # Class Object Attribute, it's a static attribute; it doesn't change
    membership = True
    def __init__(self, name='anonymous', age=0):
        if(PlayerCharacter.membership):
            self.name = name            #attribute
            self.age = age              #attribute
        
    def run(self):                  #Method
        print('run')
        
    def shout(self):
        print(f'my name is {self.name}')
        
    #Can be called without instantiating an object
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    def adding_thing2(num1, num2):
        return num1 + num2
    
        
player1 = PlayerCharacter('John', 37)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

player3 = PlayerCharacter.adding_things(3,9)
#help(player1)

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.attack)
print(player1.adding_things(2,3))
print(PlayerCharacter.adding_things(10,4))
print(player3)

player1.run()
print(player1.membership)
player1.shout()