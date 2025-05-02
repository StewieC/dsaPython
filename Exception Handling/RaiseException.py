"""
we raise an exception using the raise keyword, followed by an instance of the exception class that we want to trigger.

we can choose from built in exceptions or define our own custom exceptions by inheriting from the Exception class.  


"""

def set(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    else:
        print(f"your age is {age}")
        
try:
    set(1)
except ValueError as e:
    print(e)