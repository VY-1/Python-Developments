#Conditional Logic

is_old = False
is_licensed = True

if is_old and is_licensed:
    print("you are old enough to drive, and you have a licence!")
elif is_licensed:
    print("you can drive with supervisor!")
else:
    print("you are not of age!")
    
print('Ok')