try:
    a = int(input("enter a no: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("hello") #will execute if try successful then else will run 