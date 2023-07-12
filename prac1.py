

letter = '''Dear <|NAME|>,
You are selected!

Date: <|DATE|>
'''
name = input("What is your name?\n")
date = input("Enter the date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|DATE|>", date)

print("Good Afternoon ", name)
print(letter)
