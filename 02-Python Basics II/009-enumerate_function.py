#Enumerate function will allow the use of index and value

print("======Enumerate a string======")
for i, char in enumerate("Helllooo"):
    print(f"index: {i}: {char}")
    
print("======Enumerate a tuple======")
for i, value in enumerate((1,2,3,4,5)):
    print(f"index: {i}: {value}")
    
print("======Enumerate a list======")
for i, value in enumerate([1,2,3,4,5]):
    print(f"index: {i}: {value}")
    
    
print("======Enumerate a list of range 100 to find the index of value 50======")

for i, value in enumerate(list(range(100))):
    print(i, value)
    if(value == 50):
        print(f"Value: {value} found at index: {i}")
