# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i <= 6:
    print(i)
    i += 1 # increment i by 
    
# break statement is used to exit the loop

print("break statement")

i = 1
while i <= 6:
    print(i)
    if i == 3:
        break # exit the loop when i is 3
    i += 1 # increment i by 1