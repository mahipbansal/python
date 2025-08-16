
#list
#list is mutable(can be changed)
list= ["Mahip", 20, 16.2005, True, 'MALE' ]
a = list
print(type(a))

print(list)
print (list[0] + " is a " + list[4] + ' born on', list[2])
print("\n")

###########################################

list.append("Engineer") #add to last
list.append(2027)
print(list)
print("\n")

#######################################

list_1= [1, 2, 456, 67, 674, 343, 4, 35]
print(list_1)

list_1.sort() #sort in ascending order
print(list_1) 

list_1.reverse() #reverse a list
print(list_1)

list_1.insert(2, 84) # insert 84 at index 2
print(list_1)

list_1.pop(3) #delete element at index 3
print(list_1)

print(list_1.pop(6)) 
#delete the element and print the deleted element
print(list_1)
