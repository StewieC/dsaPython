"""
the else statement in a for loop specifies a block of code to be executed
when the loop has ended

"""

for x in range(5):
    print(x, '\n')
else:
    print("loop ended")
    
    
# else statement will not be executed if the loop is terminated by a break statement
for x in range(5):
    if x == 3:
        break
    print(x, '\n')
else:
    print("loop ended")