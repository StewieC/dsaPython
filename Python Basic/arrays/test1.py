cars = ["tesla", "ford", "toyota", "honda"]
print(cars)
print('\n')

car1 = "tesla"
car2 = "ford"
car3 = "toyota"
car4 = "honda"

# to modify an array
cars = ["tesla", "ford", "toyota", "honda"]
print(cars)
cars[0] = "audi"
print(cars)

# looping array elements
for x in cars:
    print(x)
    
# adding array elements
cars.append("mercedes")
print(len(cars))

# array methods
"""
Method	    Description

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

"""