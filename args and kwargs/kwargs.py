"""
the special syntax **kwargs in function definitions is used to pass a variable length argument list.

we use the name kwargs with double start

a keyword argument is where you provide a name to the variable as you pass it into the function

it collects all the additional keyword arguments passed to the function and stores them in a dictionary
"""

# example 1
def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))
        
fun(name="my", age=23, country="not my country")
print("\n")
# example 2
def fun(arg1, **kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))


# Driver code
fun("Hi", s1='Geeks', s2='for', s3='Geeks')