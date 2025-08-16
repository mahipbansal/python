mylist = [2, 3, 4, 5]

squarelist = []
for item in mylist:
    squarelist.append(item*item)
print(squarelist)

# or using list comprenhesion
square = [i*i for i in mylist]
print(square)