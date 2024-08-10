#Dunder methods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict ={ 'name': 'Yoyo', 'has_pets': False}
        
    #Override str method    
    def __str__(self):
        return f'{self.color} {self.age}'
        
    #Override len method
    def __len__(self):
        return 5
    
    #Override
    # def __del__(self):
    #     print('deleted!')
        
    #Override
    def __call__(self):
        return ('yess??')
    
    def __getitem__(self, i):
        return self.my_dict[i]
    
action_figure = Toy('Red', 0)
print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))
#del action_figure
#call method
print(action_figure())
print(action_figure['name'])