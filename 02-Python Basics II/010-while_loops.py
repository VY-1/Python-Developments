#While loops
print("====With break implemented, else statement doesn't get executed=====")
i = 0
while i < 50:
    print(i)
    i+=1
    break
else:
    print("done with all the work")


print("======Without break statement, else statement gets executed=====")   
i = 0
while i < 50:
    print(i)
    i+=1
    #break
else:
    print("done with all the work")
    
    
my_list = [1,2,3]

print("=====For loop====")
for item in my_list:
    print(item)
    
print("=====While Loop=====")
i=0
while i < len(my_list):
    print(my_list[i])
    i+=1
    
    
#While loop use case. When we don't know how many iteration until condition is met
print("======While loop and break usecase======")
while True:
    response = input("Say something: ")
    if(response == 'bye'):
        break
    
print("========Break, Continue, Pass=======") 
print("======Break=====")
my_list = [1,2,3]
for item in my_list:
    print(item)
    break

print("=====Continue=====")
for item in my_list:
    print(item)
    continue
    print("this line will never get printed")
    
print("======Pass=====")
for item in my_list:
    print(item)
    pass            #does nothing, mainly use as placeholder



