#For Loops
print("======Iterate a string======")
for item in 'Hi how are you doing?':
    print(item, end=" ")
  
print()

print("======Iterate a list======")
for item in [1,2,3,4,5]:
    print(item)

print("======Iterate a set======")
for item in {1,2,3,4,5}:
    print(item, end="\t")

print()
    
print("======Iterate a tuple======")
for item in (1,2,3,4,5):
    print(item, end=" ")
    
print()    
print("====Nested for loop=====")
for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)