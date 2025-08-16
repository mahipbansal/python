# dictionaries are mutable, unordered
#keys must be unique but value can be repeated
d = {} #empty dictionary
marks = {
    "harry" :100,
    "aman" : 59,
    "suman" : "kamla",
    "harish" : [1,2,3],
    "rohan" : 80
}

print (marks, type(marks))
print (marks["harry"])
print(marks["suman"])
print(marks["harish"])
print("\n")

# methods
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"harry" : 89, "suresh" : "male"})
print(marks)

print(marks.get("alpha"))# prints none if not in dict.
#print(marks["alpha"])  #returns an error