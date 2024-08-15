# High Order Function HOC, HOC is a function that accepts another function as paramerter
# or returns a function

# greet and greet2 are a higher order function
def greet(func):
    func()
    
def greet2():
    def func():
        return 5
    return func 

