# 2d Vector
"""
class C2dVec:
    def __init__(self,i,j):
         self.icap = i
         self.jcap = j
         
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j+{self.kcap}k"   

v2d = C2dVec(1,3)
v3d = C3dVec(1,3,6)

print(v2d)
print(v3d)
"""


# Animal Kingdom
"""
class Animals:
    def animalType(self):
        print("The animal type is Mammal")
    
class Pets(Animals):
    def animalColour(self):
        print("The colour of animal is White")
    
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow")
        

d1 = Dog()
d1.animalType()
d1.animalColour()
d1.bark()
""" 

#Employee and Salary
class Employee:
    salary  = 1000
    increment = 1.5
    @property
    
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter 
    
    def salaryAfterIncrement(self,sal):
        self.increment = sal/self.salary


e = Employee()
print(e.salaryAfterIncrement)

