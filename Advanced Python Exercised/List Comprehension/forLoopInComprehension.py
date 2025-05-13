a = [1, 2, 3, 4, 5]

# creating an empty list
lis = []

# iterate over each element
for i in a:
    # multiply every item by 3 and append it to lis
    lis.append(i * 3)
    
print(lis)

# using list comprehension
a = [1, 2, 3, 4, 5]

list = [i * 2 for i in a]

print(list)