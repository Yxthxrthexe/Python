#HERE THE SELF IS TAKEN AS AN INPUT IN THE CONSTRUCTOR
class Employee:
    company = "Google"
    def __init__(self):
        print("Employee is created") #CONSTRUCTOR CREATED
        
    def getSalary(self,sigh):
        print("Salary is ",self.salary,sigh)
        

sal = Employee()
sal.salary = 1000
sal.getSalary("Thanks") 