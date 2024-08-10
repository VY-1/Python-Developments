# Walrus operator; :=
# Walrus syntax := that assigns values to variables as part of a larger expression

a = 'helloooooooooooo'

if(len(a) > 10):
    print(f"too long {len(a)} elements")
    
    
print("======Walrus operator========")

if((n:=len(a)) > 10):
    print(f"too long {n} elements")

print("======Walrus operator with while loop======")
while ((n:=len(a)) > 1):
    print(n)
    a = a[:-1]
    
print(a)