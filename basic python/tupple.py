#tupple
#tupple is immutable(when changed a new tupple is formed)

t1= (1)
print(type(t1))

t2= (1,)
print(type(t2))

t =("mahip", 20, "may", 16.2005, 20, 16.2005)
print(type(t))
print(t)

t3= t.count(20) # count no of 20 in the tupple
print(t3)

i= t.index(16.2005) #index at which the element comes for 1st time
print(i)

t5 = (1, 4, 6, 9)
t6 = (3, 5, 1, 4)

t7= t6 + t5 #concatenation
print(t7)

t8 = t6 * 3 #repetition
print(t8)

print(3 in t6) #membership
print(3 in t5)

a, b, c, d = t5 #unpacking
print(t5)