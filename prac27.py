# Multiple  Inheritance
"""
class Employee:
    company = "Visa"
    def visa(self):
        print("This is for Visa")
        
class Freelancer:
    company = "Indigo"
    def indigo(self):
        print("This is for Indigo")

class Programmer(Employee,Freelancer):
    pass

p= Programmer()
p.visa()
p.indigo()
"""
# MultiLevel Inheritance

class Person:
    country = "India"
    
    def takeBreak(self):
        print("I am breathing")
        
class Employee(Person):
    company = "Honda"
    
    def getSalary(self):
        print("Salary is ",self.salary)
        
    def takeBreak(self):
        print("I am an Employee")
        
class Programmer(Employee):
    company = "Fiverr"
    
    def getSalary(self):
        print("No salary")        
        
        
p = Person()
e = Employee()
pg = Programmer()
p.takeBreak()
pg.takeBreak()