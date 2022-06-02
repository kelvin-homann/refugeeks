def harmonicSumRecursive(n):
    if n == 1:
        return 1
    else:
        return 1 / n + (harmonicSumRecursive(n - 1))


print(harmonicSumRecursive(10))
