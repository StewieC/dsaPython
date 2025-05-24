# the map function is used to apply a given function to every item of an iterable such as list or tuple

# and returns a map object(which is an iterator)

s = ['1', '2', '3', '4']

res = map(int, s)

print(list(res))

"""
here we used built in int function to convert each string in te list into integer

the map() function takes care of appying int() to every element

"""