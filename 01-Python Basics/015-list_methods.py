#List methods
basket = [1,2,3,4,5]
print(len(basket))

print("======Adding To a List=======")
#adding to a list
basket.append(100)
basket.insert(5,50)
new_list = basket
print(basket)
print(new_list)

basket.extend([101,102,103])

print(basket)
print(new_list)

print("======Removing From a List======")
#removing
basket.remove(100)      #remove integer 100 from a list
print(basket)
removed_value = basket.pop(4)           #remove base on index 4, and return value that was removed
print(f" removed value: {removed_value}")
print(basket)
removed_value = basket.pop()            #remove the last index, and return value that was removed
print(f" removed value: {removed_value}")
print(basket)
basket.clear()          #remove everything on the list
print(basket)

print("==========Find the Index=========")
basket2 = ['a', 'b', 'c', 'd', 'e', 'd', 'd', 'x']
print(basket2.index('d'))       #returns the index of content 'b'
#basket2.index(value_to_remove, starting_index, ending_index)
print(basket2.index('b', 1, 4))  # value 'b' starting index 2, end index 4

print("========Find if value in the list========")
print('d' in basket2)            #returns True
print('x' in basket2)            #returns False

print("============Find Count=============")

print(basket2.count('d'))       #returns 3

print("=======Sort=======")
sorted_basket = sorted(basket2)                 #Sorted function that returns sorted values
print(f"basket2 {basket2}")
print(f"sorted_basket {sorted_basket}")
basket2.sort()                  #sorted the list
print(basket2)

print("========Reverse========")
basket3 = ['a', 'b', 'c', 'd', 'e', 'd', 'd', 'x']
basket3.reverse()
print(basket3)
print(basket3[::-1])        #reverse again with slicing list

print("========Range========")
print(range(1,100))             #range(start, stop); 1-99, exluding stop
print(list(range(1,100)))       #Create a list of from 1 to 99
print(list(range(100)))         #Create a list from 0 to 99
print(list(range(2,100)))

print("=========Join========")
sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JO', 'Daddy'])   #returns the newly join values
print(new_sentence)

new_sentence = " - ".join(['hi', 'my', 'name', 'is', 'JO', 'Daddy'])   #returns the newly join values
print(new_sentence)

print("=======List Unpacking=======")
a,b,c, *other, d, e = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)
print(e)