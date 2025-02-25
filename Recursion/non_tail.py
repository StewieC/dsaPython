def nonTail(n):
    if n == 1:
        return 1
    else:
        return n * nonTail(n - 1)
    
print(nonTail(10))  