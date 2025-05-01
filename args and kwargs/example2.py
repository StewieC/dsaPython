def fun(arg1, *argsv):
    print("first argument: ", arg1)
    for arg in argsv:
        print("argument *argv: ",arg)
fun("my", "name", "is", "not", "my", "name")