matrix = [["apple", "banana", "cherry"],
          ["date", "fig", "grape"],
          ["kiwi", "lemon", "mango"]]

mod = []
for row in matrix:
    mod_row = []
    for fruit in row:
        mod_row.append(fruit.capitalize())
    mod.append(mod_row)
    
print(mod)
print("---------------------------------------")

# using list comprehension
matrix = [["apple", "banana", "cherry"],
          ["date", "fig", "grape"],
          ["kiwi", "lemon", "mango"]]

mod = [[fruit.capitalize()for fruit in row] for row in matrix]
print(mod)