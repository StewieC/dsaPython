"""
list comprehensions can include conditional statements to filtre or modify items based on specific criteria.

these conditionals help us create customized lists quickly and making code cleaner

"""

# to filtre all even numbers from the list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]

list1 = [i for i in a if i % 2 == 0]

list2 = [i for i in a if i % 2 == 1]

print(list1)
print(list2)

# creating a list from a range
# create a list of numbers from 0 to 10

a = [i for i in range(11)]
print(a)

# using nestedloops
# creae a list of tuples representing all combinations of (x,y) where both x and y range from 0 to 2

cord = [(x,y) for x in range (3) for y in range(3)]
print(cord)

# supposse we have many lists in a list and we want to make a single list 

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list = [i for row in a for i in row]
print(list)