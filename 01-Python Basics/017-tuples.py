#Tuple: tuples are immutable. Tuple cannot be modified, but can access its index
#Tuples are lists that are immutable.
my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

new_tuple = my_tuple[1:2]
print(new_tuple)
new_tuple = my_tuple[1:4]
print(new_tuple)


#unpacking a tuple

x,y,z, *other = (1,2,3,4,5)

print(x)
print(y)
print(z)
print(other)