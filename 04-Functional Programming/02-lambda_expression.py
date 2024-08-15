# Lambda Expressions
# function where we only need to use it once, anonymous function

# Lambda

# lambda param: action(param)
# lambda item: item * 2
my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list)))

# filter with lambda to get only_odd
print(list(filter(lambda item: item % 2 != 0, my_list)))

# reduce with lambda
from functools import reduce
print(reduce(lambda acc,item: acc + item, my_list, 10))

