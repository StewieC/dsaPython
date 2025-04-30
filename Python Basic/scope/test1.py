# A variable is only available from inside the region it is created. This is called scope.

# local scope: a variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
    x = 300
    print(x)  # This will print 300
    
myfunc()

# function inside a function:
def myfunc2():
    x = 300
    def myinnerfunc():
        print(x)  # This will print 300
    myinnerfunc()
myfunc2()