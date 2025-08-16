f = open("file_function.txt", "r")

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line1, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

lines = f.readlines()
print(lines, type(lines))

f.close()