#Exercise Password Checker

username = input("Enter your username: ")
password = input("Enter your password: ")

print("{}, your password {} is {} letters long".format(username, "*"*len(password), len(password)))