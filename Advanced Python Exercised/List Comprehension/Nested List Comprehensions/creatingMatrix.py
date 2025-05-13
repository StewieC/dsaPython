# creating a matrix without list comprehension
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(i * j)
        
print(matrix)

# using list comprehension
matrix = [[j for j in range(5)]for i in range(5)]
print(matrix)