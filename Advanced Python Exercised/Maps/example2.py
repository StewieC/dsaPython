# by default, the map function returns a map object which is an iterator

# in many cases we convert the iterator to a list to work with results directly

# lets double each element in a list

a = [1, 2, 3, 4, 5]

# create a function that simply doubles the provided number
def double(val):
    return val*2

res = list(map(double, a))
print(res)

# the nap function returned an iterator which we then converted into a list using list()

# map() using a lambda function instead of a custom function with map()

res = list(map(lambda x: x*2, a))
print(res)
