# Objects And Class Implementation

class Employee:
    company = "Google"
    salary = 100
    

harry = Employee()
raj = Employee()
harry.salary= 300
raj.salary= 400
print(harry.company) # TO PRINT THE VARIABLE OUTSIDE THE CLASS "HARRY" OBJECT IS USED!
print(raj.company)
Employee.company='Youtube'
print(harry.company)
print(harry.salary) 
print(raj.salary)
