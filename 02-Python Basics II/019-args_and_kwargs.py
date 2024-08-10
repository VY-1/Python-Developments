# *args **kwargs


def super_func(*args):      #*args indicate multi positional arguments
    return sum(args)


print(super_func(1,2,3,4,5))


print("=====*args===")

def super_func(*args):      #*args indicate multi positional arguments
    print(*args)
    print(args)             #prints tuple
    return sum(args)


print(super_func(1,2,3,4,5))

print("=====**kwargs===")

def super_func(*args, **kwargs):      #**kwargs indicate multi positional keyword arguments
    total = 0
    print(*args)
    print(args)             #prints tuple
    #print(**kwargs)        #Error out
    print(kwargs)           #prints dictionary
    for item in kwargs.values():
        total += item
        
    return sum(args) + total


print(super_func(1,2,3,4,5, num1=5, num2=10))

#Rule: params, *args, default parameters, **kwargs
print("=====Rule of order=====")

def super_func(name, *args, i='hi', **kwargs):
    total = 0
    print(*args)
    print(args)             #prints tuple
    #print(**kwargs)        #Error out
    print(kwargs)           #prints dictionary
    for item in kwargs.values():
        total += item
        
    return f'{i} {name} the sum is: {sum(args) + total}'


print(super_func('Andy', 1,2,3,4,5, num1=5, num2=10))
