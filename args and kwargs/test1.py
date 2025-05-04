# *args and *kwargs are used to allow functions to accept arbitrary number of arguments
def fun(*args):
    return sum(args)
print(fun(1,2,3,4,5))

"""
if we want to make a multiply function that takes any number of argumrnts,
it can be done using *args

using *, the variable that we associate witht the  * becomes iterable"""

def multiply(*argsv):
    for arg in argsv:
        print(arg)
multiply("my", "name", "is", "not", "my", "name")