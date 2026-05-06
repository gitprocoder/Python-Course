A = [1,8,7,2,21,15]

# updates the list to [1,2,7,8,15,21]
A.sort() #it is a function
print(A)

# updates the list to [15,21,2,7,8,1]
A.reverse()
print(A)

# adds 3 at the end of the list.
A.append(3)
print(A)

# This will add 8 at 1 index
A.insert(1,8)
print(A)

# Will delete element at index 2 and return its value
A.pop(2)
print(A)

# Will remove 21 from the list.
A.remove(21)
print(A)