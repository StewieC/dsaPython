# handling a simple exception

n = 3
try:
    print(n / 0)
except ZeroDivisionError:
    print("cant do that pal")
    
"""
difference btn exception and error:

error: are serious issues that a program shouldnt try to handle.
        usually a programmer error, such as syntax error or a type error.
        
        
exception: are events that can be handled by the program.
        they are usually caused by external factors, such as invalid input, missing files  or network issues.
"""