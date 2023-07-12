# INHERITANCE

class Employee:
    classmethodompany = "Google"
    
    def showDetails(self):
        print("Hello!!!")
    

class Programmer(Employee):  #(programmer class is the child of Employee)
    language = "Python"    #Single Level Inheritance
    
    def getLanguage(self):
        print("The language is ",self.language)


e = Employee()
p = Programmer()
p.showDetails()
p.getLanguage()