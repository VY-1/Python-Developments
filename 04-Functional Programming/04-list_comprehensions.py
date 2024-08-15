#List, Set, and Dictionary Comprehensions


# Standard way
my_list = []

for char in 'hello':
    my_list.append(char)
    
print(my_list)

print("=========List Comprehension==========")
# List comprehension
#my_list = [param for param in iterable]

my_list = [char for char in 'hello']
print(my_list)

# generate a list of value from 0-99
my_list2 = [num for num in range(0,100)]
print(my_list2)

# generate a list of value from 0-99 time each number by 2
my_list3 = [num*2 for num in range(0, 100)]
print(my_list3)

# generate a list of value from 0-99 time each number by 2, but keep only even number
my_list4 = [num*2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)

#----------------------------------
print("=========Set Comprehension=========")
# Set Comprehension
my_list = {char for char in 'hello'}
print(my_list)

# generate a set of value from 0-99
my_list2 = {num for num in range(0,100)}
print(my_list2)

# generate a set of value from 0-99 time each number by 2
my_list3 = {num*2 for num in range(0, 100)}
print(my_list3)

# generate a set of value from 0-99 time each number by 2, but keep only even number
my_list4 = {num*2 for num in range(0, 100) if num % 2 == 0}
print(my_list4)


#---------------------------------
print("==========Dictionary Comprehension=========")
# Dictionary Comprehension
# my_dict = {key: value}

simple_dict = {
    'a': 1,
    'b': 2
}

# multiply value by 2
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
print(my_dict)

# Using dictionary comprehension, to create a dictionary from a list of value; key=value, value=value*2

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)