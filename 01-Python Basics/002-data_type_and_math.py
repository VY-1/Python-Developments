#Fundamental Data Types
int
float
bool
str
list
tuple
set
dict

#Classes -> Custom Data Types

#Specialized Data Types

None

#----------------------------------------
#Fundamental Data Types
#integer and float
print("======== Integer and Float========")
print(2 + 4)
print(2 - 5)
print(2 * 4)
print(2 / 4)

print(type(2 + 4))     #int
print(type(2 - 5))     #int
print(type(2 * 4))     #int
print(type(2 / 4))     #float
print(type(5.0))       #float

print(2 ** 2)       #2 to the power of 2
print(2 // 4)       # // will round down to integer =0
print(5 // 4)       # rounds down to integer = 1
print(type(2 // 4)) #int data type
print(type(5 // 4)) #int data type

print( 5 % 4)       # % will produce remainders


print()
# math functions
print("=======Math Function=======")
print(round(3.1))   #round down to the nearest whole number in int
print(round(3.9))   #round up to the nearest whole number in int

print(type(round(3.1)))
print(type(round(3.9)))
print(abs(-20))