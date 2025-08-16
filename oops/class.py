#class contains information 
class employee: #info same for all
    language = "Python" #class attribute
    salary = 10000000
    def getinfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")
    
    def greets(self):
        print("good morning")

    @staticmethod
    def greet():
        print("good evening")

# object

person1 = employee()
person1.name = "Mahip Bansal" #object/instance attribute
print(person1.name)
print(person1.language)
print(person1.salary)

person2 = employee()
person2.name = "Anay Bansal"
person2.language = "Java"
print(person2.name, person2.salary, person2.language)

person2.getinfo()
person1.greets()
person1.greet()