#Iterables
#Iterable - list, dictionary, tuple, set, string
#iterate -> one by one check each item in the collection

user = {
    "name": 'Golem',
    "age": 5006,
    "can_swim" : False
}

print("=====items()======")
#Items will return key,values pair
for item in user.items():
    print(item)
    
print("=====keys()======")

#keys will return keys
for item in user.keys():
    print(item)
    
print("=====values()=====")
#values will return values
for item in user.values():
    print(item)
    
print("=====unpacking tuple======")
for item in user.items():
    key, value = item
    print(key, value)

print("====short hand unpacking====")
for key, value in user.items():
    print(key, value)
