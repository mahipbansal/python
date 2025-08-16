
a = int(input("enter 1st no: "))
b = int(input("enter 2nd no: "))

if(b==0):
    raise ZeroDivisionError("hey our program can't divide any no by zero('0')")
else:
    print(f"the division of {a}/{b} is {a/b}")

print("hey")