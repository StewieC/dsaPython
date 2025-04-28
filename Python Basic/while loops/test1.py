# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i <= 6:
    print(i)
    i += 1 # increment i by 
    
# break statement is used to exit the loop

print("end", '\n')

i = 1
while i <= 6:
    print(i)
    if i == 3:
        break # exit the loop when i is 3
    i += 1 # increment i by 1
    
print("end of loop", '\n')

# continue statement is used to skip the current iteration and move to the next iteration
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# else can run a code blck when the condition is not true

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")