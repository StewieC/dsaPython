def tail(n, acc=1):
    # Base case
    if n == 0:
        return acc
    # Recursive case
    else:
        return tail(n-1, n*acc)
    
print(tail(5))  # 120