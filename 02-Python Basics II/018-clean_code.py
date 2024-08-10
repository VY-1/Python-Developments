# Clean Code

def is_even(num):
    if num % 2 == 0:
        return True
    
    return False
    

print(is_even(50))
print(is_even(51))

print("=======Clean Code======")
#Clean code
def is_even(num):
    return num % 2 == 0
    
    
print(is_even(50))
print(is_even(51))