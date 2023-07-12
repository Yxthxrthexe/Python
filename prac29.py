"""
COMPLEX NO. ADDITION and MULTIPLY
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i
    
    def __add__(self,c):
        return Complex(self.real + c.real, self.img + c.img)
    
c1 = Complex(1,4)
c2= Complex(8,5)

print (c1 +c2)
"""

"""
MULTIPLICATION AND ADDITION OF TWO COMPLEX NO.
class Complex:
    def __init__(self):
        pass
    def add(self,r1,c1,r2,c2):
        print("The addition is ",r1+r2," + ",c1+c2,"i") 
    def mul(self,r1,c1,r2,c2):
        print("The multiplication is ",(r1*r2) - (c1*c2)," + ",(r1*c2) + (r2*c1),"i")

c = Complex()
c.add(2,1,4,3)
c.mul(2,1,4,3)
"""

class Vector:
    def __init__(self):
        pass
    def sum(self,i1,j1,k1,i2,j2,k2):
        print("The addition of two vectors are ",(i1+i2),"i + ",(j1+j2),"j + ",(k1+k2),"k + ",)
    def mul(self,i1,j1,k1,i2,j2,k2):
        print("The multiplication of two vectors are ",(i1*i2)+(j1*j2)+(k1*k2))
        
v = Vector()
v.sum(1,2,3,4,5,6)
v.mul(1,2,3,4,5,6)