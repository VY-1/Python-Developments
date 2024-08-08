#String 

print("=========STRING========")

"this is a string"

type1 = type("this is a string")

print(type1)

# can be use with single quote or double quotes

username= 'coder'
password = "secretcode"

# Long string can be used with triple quotes

long_string = '''This is a long string

It an be as long as you like and can be used with multiple lines.

WOW'''

print(long_string)

print("=========STRING CONCATEGNATION=========")

# String concatenation
first_name = "Joe"
last_name = "Mamma"
full_name = first_name + " " + last_name

print(full_name)

# String concat only works with string
#print('hello' + 5)     #will fail


print("=======STRING CONVERSION/CASTING========")
# type conversion
print('hello' + str(5))     #will need to cast 5 to a string type to be concat

print(str(100))     #String of 100
print(type(str(100)))   #Type convert int to string


print("========ESCAPE SEQUENCE==========")

#Escape Sequence
weather = 'It\'s \'kind of\' sunny.... backslash=\\'     #escape the character with backslash
print(weather)

print("\n\n\n")

#Escape Sequence with predefined keywords like \n \t
weather = "\t It\'s \"kind of\" sunny \n hope you have a good day!"
print(weather)



print("========FORMATTED STRINGS========")
#Formatted Strings

name = 'Johnny'
age = 55
print(f"Hi {name}, you are {age} years old")      #add f in front of the string

print("Hi {}, you are {} years old".format("Mike", "60"))   #can also be done
print("Hi {}, you are {} years old".format(name, age))   #can also be done

#can change the order
print("Hi {1}, you are {0} years old".format(name, age))   #can also be done

print("Hi {new_name}, you are {age} years old".format(new_name="Sally", age=100))   #can also be done

print("=========STRING INDEX=========")
#String index
selfish = "me me me"
    #index 01234567
    
#[start:stop]
#[start:stop:stepover]      #by default, stepover =1
print(selfish[0])       #grap index 0
print(selfish[7])
print(selfish[0:2])

print("\n\n")
string_idx = '01234567'
print(string_idx[0:2])
print(string_idx[0:4])
print(string_idx[0:8])

print()
print(string_idx[0:8:1])
print(string_idx[0:8:2])    #Stepover by 2;  0246

print()
print(string_idx[1:])       #print from index 1 to end
print(string_idx[:8])       #print from begining index 0 to 8
print(string_idx[:4])       #print from begining index 0 to 4; 0123
print(string_idx[::1])      #print all and stepover by 1
print(string_idx[-1])       # the -1 means start at the end of the string
print(string_idx[-2])
print(string_idx[-3])
print()

print(string_idx[::-1])     #Stepover from the end, reverse the string.. commonly used for reverse order
print(string_idx[::-2])     #Stepover by 2 in reverse order

#Immutabilitiy
#Strings are immutable

#cannot change index, but can reassign the whole string content; immutable
#string_idx[0] = '8'