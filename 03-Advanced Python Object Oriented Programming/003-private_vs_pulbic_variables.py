#Private vs Public Variables

class PlayerCharacter:
    # Class Object Attribute, it's a static attribute; it doesn't change
    membership = True
    def __init__(self, name='anonymous', age=0):
        if(PlayerCharacter.membership):
            self._name = name            #private attribute variable
            self._age = age              #private attribute variable
        
    def run(self):                  #Method
        print('run')
        
    def shout(self):
        print(f'my name is {self._name}')
        
        
player1 = PlayerCharacter("Joe", 45)
player1.age = 23

print(player1._age)
print(player1.age)

player1._age = 21
print(player1._age)