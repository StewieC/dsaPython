def printNumbers(n):
    if n == 0:
        return
    print(n)
    printNumbers(n - 1)

printNumbers(10)  # 10 9 8 7 6 5 4 3 2 1