# FUNCTIONS
""""
Q-1
def percent(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100


marks1 = [45, 78, 86, 77]
percentage = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage1 = percent(marks2)

print(percentage, "/n", percentage1)
"""
import n1 as n1

# Q-2
"""
def greet(name):
    print("Hello ", name)


def sum(num1, num2):
    print(num1 + num2)


nme = input("What is ur name??")
n1 = int(input("Enter value1"))
n2 = int(input("Enter value2"))
greet(nme)
sum(n1, n2)
"""

# Q-3
"""
def factorial(n1):
    ft = 1
    for i in range(1, n1 + 1):
        ft = ft * i
    return ft


num = int(input("Factorial of -->"))
f1 = factorial(num)
print(f1)
"""

# Q-4

"""
def fact1(n1):
    if n1 == 1 or n1 == 0:
        return 1
    return n1 * fact1(n1 - 1)


num = int(input("Factorial of -->"))
f = fact1(num)
print(f)
"""

# Q-5
