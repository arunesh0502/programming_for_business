A = {"a", 1, 4.5}
B = {"b", 2, 4.5}

print(A|B)

print(A-B)

print(A^B)

print(A&B)

#a. tuple_one + list_one
#b. tuple_one + tuple(list_one)
#c. list_one[1] = 4.2
#d. tuple_one[1] = 4.2

tuple_one = ('Hello', 42) 
list_one = ['Hello', 42]

#print(tuple_one + list_one) # returns error when executed
print(tuple_one + tuple(list_one))
list_one[1] = 4.2
print(list_one)