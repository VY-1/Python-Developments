# Creating Our Own Objects

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
        
player1 = PlayerCharacter('John', 37)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

#help(player1)

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.attack)


player1.run()
print(player1.membership)
player1.shout()

