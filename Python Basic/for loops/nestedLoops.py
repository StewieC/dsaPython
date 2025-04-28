# in a nested loop: the inner loop is executed once for each iteration of the outer loop

colors = ["red", "green", "blue"]
fruits = ["apple", "banana", "cherry"]

for x in colors:
    for y in fruits:
        print(x, y)