# set

a = {1, 2, 3, 4, 5, 1}

# Set don't print the repeated the values!!
print(a.pop())  # prints the first element that is poped
print(type(a))
print(a)
# a={ } : This syntax will create an empty dictionary and not an empty set !!

# Empty Set\\

b = set()
b.add(4)
b.add(5)  # To add the elements in the set
b.add(99)
b.remove(5)
print(b.intersection(a))  # Intersection of A and B sets
print(b.union(a))
# b.clear()  # clears the set
print(type(b))
print(b)
print(len(b))
