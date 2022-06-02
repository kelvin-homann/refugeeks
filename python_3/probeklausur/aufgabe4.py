def harmonicSumRecursive(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonicSumRecursive(n - 1))


print(harmonicSumRecursive(10))
