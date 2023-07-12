# Q-1 
#roomiesarah
class Programmer:
    company ="Microsoft"
    def __init__(self):
        pass
    
    def  info(self,name,product):
        print("The name of the programmer is ",name," and the product is ",product)
        
sal = Programmer()
sal.info("Yatharth","Github")


# Q-2
class Calculator:
    
    def __init__(self):
        pass
    
    def add(self,a,b):
        print("The addition of ",a," and ",b," is ",a+b)
        
    def sub(self,a,b):
        print("The subtraction of ",a," and ",b," is ",a-b)
    
    def mul(self,a,b):
        print("The addition of ",a," and ",b," is ",a*b)
        
    def div(self,a,b):
        print("The addition of ",a," and ",b," is ",a/b)
    def sqr(self,a,b):
        print("The Square root of ",a," and ",b," is ",pow(a,1/2)," and ",pow(b,1/2))  

cal = Calculator()

n1 = int(input("Enter the value of first number"))
n2 = int(input("Enter the value of second number"))
i=1
while(i<100):
      
    num =int(input("Press-->1 Addition, Press-->2 Subtraction, Press-->3 Multiplaction, Press-->4 Division, Press-->5 Square Root"))
    if num ==1 :
      cal.add(n1,n2)
    elif num ==2 :
      cal.sub(n1,n2)
    elif num ==3 :
      cal.mul(n1,n2)
    elif num ==4 :
      cal.div(n1,n2)
    elif num ==5 :
      cal.sqr(n1,n2)
    else:
       print("Invalid Input")