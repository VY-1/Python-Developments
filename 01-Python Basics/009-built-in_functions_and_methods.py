
#Built-in functions

greet = 'hellloooo'
print(greet[:len(greet)])

#Built-in methods


greet.format()

quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))         #method to find index of 'be'
print(quote.replace('be', 'me'))

print(quote)                    #will display the original string since strings are immutable