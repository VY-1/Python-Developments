
# Pure Function

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    
    return new_list

print(multiply_by2([1,2,3]))

print("=======Functional Programming========")
# Functional Programming paradigm
# map, filter, zip, and reduce

# map(action, iterable)
def multiply_num_by2(item):
    return item*2

print(list(map(multiply_num_by2, [1,2,3])))

# filter(action, iterable)
def only_odd(item):
    return item % 2 != 0

my_list = [1,2,3]
print(list(filter(only_odd, my_list)))

# zip(iterable, iterable2, iterable3,....)
my_list = [1,2,3]
your_list = [10,20,30]

print(list(zip(my_list, your_list)))

# reduce(accumulator, iterable, startValue)
from functools import reduce

my_list = [1,5,3,2,6]
def accumulator(acc, item):
    #print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))
print(reduce(accumulator, my_list, 10))

