class hello:
    language = "Python" #class attribute
    salary = 10000000

    def __init__(self): #dunder method(which is automatically called)
        print("hi how are you")

    def __init__(self, name, salary, language):
        self.name= name
        self.salary = salary
        self.language = language
        print("hello")

mahip = hello("Mahip", 2000000, "python")
print(mahip.name, mahip.salary, mahip.language)