try:
    a = int(input("enter a no: "))
    print(a)
except Exception as e:
    print(e)
finally:
    print("hey there") #will always run/execute