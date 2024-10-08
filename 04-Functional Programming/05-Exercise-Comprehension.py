# Exercise with List comprehension

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
            
print(duplicates)

print("=========List Comprehension=========")
# Do the same using list comprehension
dup = list(set([value for value in some_list if some_list.count(value) > 1]))
print(dup)