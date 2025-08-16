
def avg(): #Function definition
    a = int(input())
    b = int(input())
    c = int(input())

    average = (a+b+c)/3
    print("avg =", average)

print("hi, please enter 3 no. to find the avg of all")
avg() #Function Call
print("thankyou")



#Function with arguments
def goodday(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "abc"

goodday("mahip", "Thankyou" )
a = goodday("hii", "there")
print(a)