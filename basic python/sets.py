# In set don't repeat elements, unordered, immutable
h = set() #empty set
print(type(h))

s = { 1, 2, 3, 79, 75, 3, 3, 3, "shankar"}
print(s)

s.add(566)
s.add("mahip")
print(s)
s.remove(566)
print(s)
s.pop() #removes 1st element
print(s)

s1= {1, 4, 5, 6}
s2= {2, 3, 4, 6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)