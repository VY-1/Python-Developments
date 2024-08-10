#Return function
def sum(num1, num2):
    return num1 + num2

total = sum(10, 5)
print(sum(10, total))

print("=========Nested Function========")
#Nested function

def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    
    return another_func

total = sum(10, 20)
print(total(10,20))

print("=========Nested Function========")
#Nested function

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    
    return another_func(num1, num2)

total = sum(10, 20)
print(total)
