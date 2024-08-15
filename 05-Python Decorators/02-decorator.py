# Decorator; decorator supercharges our functions



def my_decorator(func):
    def wrap_func(*args, **kwarg):
        print('************')
        func(*args, **kwarg)
        func(*args, **kwarg)
        print('************')
    return wrap_func    # does not execute, only return wrap_func


#Using my_decorator function on the hello function
@my_decorator
def hello():
    print('helllloooo')
    
    
hello()

# under the hood

def bye():
    print('bye, see ya later, playa')
    
    
byebye = my_decorator(bye)      # assigning decorator function to byebye variable

byebye()                        # executing byebye as a function

#using method with arguments
@my_decorator
def hello2(greeting, emoji=":>"):
    print(greeting, emoji)

hello2("hi")
