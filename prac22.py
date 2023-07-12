class Employee:
    company = "Google"
    def getSalary(self,sigh):
        print("Salary is ",self.salary,sigh)
    
    @staticmethod
    def greet(): #self not needed in the static method
        print("Good morning,Sir")
     
    @staticmethod
    def time():
        print("The time is 9 A.M")   
        
sal = Employee()
sal.salary = 1000
sal.getSalary("Thanks")
sal.greet()
sal.time()