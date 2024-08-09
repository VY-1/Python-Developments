#Functions

def say_hello():
    print("helllloooo")
    
say_hello()

#display the function in memory
print(say_hello)

hi = say_hello      #store function in variable
hi()                #execute variable as function


#Function with parameters
def say_hi(name, emoji):
    print(f"Hi {name} {emoji}")
    
# Call function with positional arguments
say_hi("Joe", "😆")

# keyword arguments
say_hi(emoji="😆", name="Dan")      #Bad practice
say_hi(name="Jill", emoji="😆")     #Good practice