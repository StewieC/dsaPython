matrix = [["apple", "banana", "cherry"], ["date", "fig", "grape"], ["kiwi", "lemon", "mango"]]

flat = []
for i in matrix:
    for j in matrix:
        flat.append(j)
print(flat)