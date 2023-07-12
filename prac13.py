num = int(input("Enter the number: "))
booli = False
for i in range(2, num):
    if num % i == 0:
        booli = True
        break
if booli == True:
    print("This is a prime number!!")
else:
    print("This is not a prime number!!")
