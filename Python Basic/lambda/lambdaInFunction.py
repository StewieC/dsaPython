"""
lambda is better shown when you use tem as anonymous function inside another function

"""

def mfunc(x):
    return lambda a : a * x

doubler = mfunc(2)
tripler = mfunc(3)
print(doubler(11))  # Output: 22
print(tripler(11))  # Output: 33
# the lambda function is used to create a function that takes one argument (a) and returns the product of a and x, where x is the value passed to mfunc when it is called.