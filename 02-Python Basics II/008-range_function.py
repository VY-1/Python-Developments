#Range function

print(range(0,100))


for number in range(0, 10):
    print(number)

#Reverse the range 
for _ in range(10, 0, -1):
    print(_)
    
#Reverse range by stepover
for _ in range(10, 0, -2):
    print(list(range(_)))