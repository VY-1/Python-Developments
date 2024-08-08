#Dictionary
dictionary = {
    'a':1,
    'b':2
}

print(dictionary['b'])
print(dictionary)           #return unorder value pairs

dictionary2 = {
    'a':[1,2,3],
    'b':"hello",
    'x': True
}

print(dictionary2)
print(dictionary2['a'][1])

#List containing dictionaries
my_list = [
    {
    'a':[1,2,3],
    'b':"hello",
    'x': True
    },
    {
    'a':[4,5,6],
    'b':"hello",
    'x': True
    }
]

print(my_list)
print(my_list[1])
print(my_list[0]['a'][2])

user = {
    'basket':[1,2,3],
    'greet':'hello'
}

#None

print(user['basket'])
#print(user['age'])     #Will error out since 'age' doesn't exist
#Preferred way
print(user.get('age'))  #Will not error out, but return 'None' since it doesn't exist
# get method can be use to return default value if not found
print(user.get('age', 21))  #Returns default value of 21 if not found
print(user.get('greet', 'hi'))

print('hello' in user.values())
print('greet' in user.keys())
print(user.items())         #display in a tuple

copy_user = user.copy()     #returns a copy of the user dictionary
print(user)
print(copy_user)

print(copy_user.pop('greet'))      #Removes key pair 'greet', and returns value removed
print(copy_user.update({'age': 21}))    #update or add key value pairs
print(copy_user)

#Create a dictionary using dict function
user2 = dict(name='Jo Mamma', age=23)
print(user2)

