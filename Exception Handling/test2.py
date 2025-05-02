# try, excep, else and finally blocks

try:
    n = 3
    print(n / 0)
    
except ZeroDivisionError:
    print("cant do that pal")
    
except ValueError:
    print("input a valid number")
    
else:
    print("this will run if no exception is raised") 
       
finally:
    print("this will always run, even if an exception is raised")