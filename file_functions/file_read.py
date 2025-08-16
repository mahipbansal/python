f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

#alternate by using "with"

with open("file.txt", "r") as f:
    print(f.read())

#using with there is no need to close the file