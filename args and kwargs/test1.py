# *args and *kwargs are used to allow functions to accept arbitrary number of arguments
def fun(*args):
    return sum(args)
print(fun(1,2,3,4,5))
