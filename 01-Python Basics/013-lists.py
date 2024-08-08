#Lists in python

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# Data Structure

cart = ['notebook', 'sunglasses', 'toys', 'grapes']

print(cart[0])

print("==========SLICING=========")
#List slicing
#[start:stop:stepover]
print(cart)
print(cart[0::2])
print(cart[::-1])       # print in reverse order with stepover by 1
print(cart[::-2])       # print in reverse order with stepover by 2
print(cart[-3:])        # print from -3 to end; same as from 1 to end
print(cart[-3::-1])     # print from -3 to end in reverse order; index 1, then index 0
print(cart[0:3])

#Lists are mutable... can be changed
cart[0] = 'laptop'
print(cart)

print("======COPY FROM SLICING========")
#List copying from slicing
new_cart = cart[0:3]
print(new_cart)
new_cart[0] = 'gum'
print(new_cart)

print("======ASSIGNING REFERENCE========")
#Will not copy, but instread assign to list in that memory
new_cart2 = cart        #will use it as reference instead
new_cart2[0] = 'paper'  #modifying new_cart2 will also modify its reference
print(cart)
print(new_cart2)

print("=======COPY List=======")
#To copy the whole list, use list_name[:]
new_cart3 = cart[:]
new_cart3[0] = 'matches'
print(cart)
print(new_cart3)