def fun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
fun(1,2,3, name="stewie", age=21)