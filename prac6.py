myDic = {
    "Fast": "In a Quick Manner",
    "Yatharth": "A Chad",
    "Marks": [12, 32, 45],
    "anotherDic": {'harry': 'Player'},
    1: 2
}

print(myDic['Yatharth'])
print(myDic[1])
print(myDic['anotherDic']['harry'])

updateDic = {
    "Rahul": "Singer"
}
myDic.update(updateDic)
# Dictionary Methods

print(list(myDic.keys()))  # prints the key of the dictionary
print(myDic.values())
print(myDic.items())  # both keys and values of dictionary
