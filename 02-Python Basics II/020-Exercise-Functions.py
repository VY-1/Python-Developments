#Exercise Function; find the highest even number

def highest_even(li):
    highest_even_number = 0
    for num in li:
        if num % 2 == 0:
            if num > highest_even_number:
                highest_even_number = num
    return highest_even_number

print(highest_even([10,2,3,4,8,11]))


print("=====Alternative=====")

def highest_even(li):
    evens = []
    for num in li:
        if num % 2 == 0:
            evens.append(num)
            
    return max(evens)

print(highest_even([2,10,2,3,4,8,11]))
