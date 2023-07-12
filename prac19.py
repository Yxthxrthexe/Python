"""
Q-1
f = open('Yatharth.txt','r')
a = f.read()
if 'how' in a:
    print("how is present")
else:
    print("how not present")
f.close()
"""


"""
Q-2
HIGHSCORE WILL BE UPDATED
def game():
    return 64

score = game()
with open("highscore.txt") as f:
    highscore = int(f.read())

if highscore<score:
    with open("highscore.txt","w") as f:
        f.write(str(score)) 
"""


"""
Q-3
MULTIPLICATION OF TABLE
for i in range(2,21):
    with open(f"tables/Multiplication_table_of_{i}","w") as f:
        for j in range(1,11):
           f.write(f"{i}x{j}={i*j}\n")
    break
"""

"""
Q-4
with open("hello.txt") as f:
    x = f.read()

x = x.replace("donkey","########")

with open("hello.txt","w") as f:
    f.write(x)
"""

"""
Q-5
file1 = 'copy.txt'
file2 = 'this.txt'
with open(file1) as f:
    x = f.read()
with open(file2) as f:
    y = f.read()
     
if x == y:
    print("Files are identical")
else:
    print("Files are identical")
"""


"""
Q-6
Copy Content from one file to another

import os
 
oldname = "Yatharth.txt"
newname = "hello.txt"
with open(oldname) as f:
    x = f.read()
    
with open(newname,"w") as f:
    f.write(x)

os.remove(oldname)
"""