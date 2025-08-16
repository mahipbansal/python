class employee:
    company = "ITC"
    name= "default name"
    salary = 2000000
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

#class programmer:
 #   company ="ITC INFO Tech"
  #  def show(self):
  #      print(f"the name of the employee is {self.name} and the salary is {self.salary}")

   # def showlanguage(self):
   #     print(f"the name of the employee is {self.name} who is good in {self.language}")

   # or using inheritance
class programmer(employee):
    company = "Itc info tech"
    language = "python"
    def showlanguage(self):
        print(f"the name of the employee is {self.name} who is good in {self.language}")

a = employee()
b = programmer()
print(a.company, b.company)
a.show()
b.showlanguage()
b.show()