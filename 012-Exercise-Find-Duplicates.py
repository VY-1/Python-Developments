#Exercise: Check for duplicates in list:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
map_list = {}
dup_list = []
for i, element in enumerate(some_list):
    if(some_list[i] in map_list):
        increase_count = map_list.get(element) + 1
        map_list.update({element: increase_count})
        if(map_list.get(element) > 1):
            dup_list.append(element)
    else:
        map_list.update({element: 1})

print(dup_list)


print("========Alternative========")
#Alternative


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in some_list:
    if some_list.count(value)> 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)