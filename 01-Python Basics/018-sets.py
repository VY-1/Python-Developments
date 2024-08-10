# Set: sets are unorder collection of unique objects. Only 1 unique object can exist in a set,
# cannot have duplicate copy. Uses curly bracket like dictionary, but without the key value pairs


my_set = {1, 2, 3, 4, 5, 5, 5, 5}

# will only return {1,2,3,4,5}; unique elements are return, no duplicates
print(my_set)

my_set.add(1)
my_set.add(10)
my_set.add(15)
my_set.add(3)
print(my_set)


# Convert list to set
# list with dup values
my_list = [1, 2, 3, 4, 5, 5, 3, 7, 9, 3, 6]

# Convert to a set of unique values
my_new_set = set(my_list)
print(my_new_set)
# Convert a set back to list
my_new_list = list(my_new_set)
print(my_new_list)
# Copy of new set
copy_new_set = my_new_set.copy()
print(copy_new_set)


my_set = {1, 2, 3, 4, 5, 5, 5, 5}
print(1 in my_set)
print(len(my_set))
